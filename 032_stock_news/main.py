import os
import requests
from datetime import date
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# get stock

stock_endpoint = "https://www.alphavantage.co/query"
stock_api_key = os.environ.get("STOCK_API_KEY")

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": str(stock_api_key)
}

stock_response = requests.get(stock_endpoint, params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
stock_list = [value for (key, value) in stock_data.items()]

yesterday_stock = float(stock_list[0]["4. close"])
day_before_yesterday_stock = float(stock_list[1]["4. close"])

difference = yesterday_stock - day_before_yesterday_stock
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference / yesterday_stock) * 100, 2)

# get news

if abs(diff_percent) > 5:
    news_endpoint = "https://newsapi.org/v2/everything"
    news_api_key = os.environ.get("NEWS_API_KEY")
    today = date.today()

    news_parameters = {
        "function": "TIME_SERIES_DAILY",
        "q": "tesla",
        "from": today,
        "sortBy": "publishedAt",
        "apiKey": str(news_api_key)
    }

    news_response = requests.get(news_endpoint, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"][:3]

    formatted_articles = [f"{STOCK}: {up_down}{diff_percent}% \nHeadline: {article['title']}. \n" \
                          f"Brief: {article['description']}" for article in news_data]

    # send sms

    twilio_sid = os.environ.get("TWILIO_SID")
    twilio_auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    client = Client(twilio_sid, twilio_auth_token)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+123456789",
            to="+123456789"
        )
