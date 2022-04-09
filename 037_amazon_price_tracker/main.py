import requests
import lxml
from bs4 import BeautifulSoup
import smtplib
import os

PRICE = 600
ITEM = "Your item"
product_url = "https://www.amazon.co.uk/your-item/"
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

header = {
    "User-Agent": "Your user agent",
    "Accept_Language": "Your accepted language"
}

response = requests.get(product_url, headers=header)
soup = BeautifulSoup(response.content, "lxml")
product_price = soup.find("span", class_="a-price-whole").text.split(".")[0]

if int(product_price) < PRICE:
    with smtplib.SMTP("your_smtp_address", port=587) as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Price Drop\n\n{ITEM} is now available for £{product_price}: {product_url}"
        )
