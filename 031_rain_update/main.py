import requests

EMAIL = "test@test.com"
PASSWORD = "test"

parameters = {
    "lat": 55.953251,
    "lon": -3.188267,
    "appid": "123456789",
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()

weather_slice = data["hourly"][:12]
umbrella_needed = False

for hour_data in weather_slice:
    condition_code = int(hour_data["weather"][0]["id"])
    if condition_code < 700:
        umbrella_needed = True

if umbrella_needed:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(EMAIL, PASSWORD)
    connection.sendmail(
        from_addr=EMAIL,
        to_addrs=EMAIL,
        msg="Subject:Bring Umbrella\n\nIt's going to rain today."
    )
