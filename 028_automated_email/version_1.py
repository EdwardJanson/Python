import smtplib
import datetime as dt
import random

my_email = "test@gmail.com"
password = "test"

now = dt.datetime.now()
day_of_week = dt.datetime.weekday(now)

if day_of_week == 0:
    with open("quotes.txt", "r") as quotes:
        quote_list = quotes.readlines()
        random_quote = random.choice(quote_list)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="test@test.com",
            msg=f"Subject:Quote\n\n{random_quote}"
        )
