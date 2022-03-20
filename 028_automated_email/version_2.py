import datetime as dt
import pandas as pd
import random
import smtplib

now = dt.datetime.now()
today = (now.month, now.day)

data = pd.read_csv("birthdays.csv")
bd_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}

if today in bd_dict:
    bd_person = bd_dict[today]
    random_number = random.randint(1, 3)
    with open(f"./letter_templates/letter_{random_number}.txt") as letter:
        bd_letter = letter.read()
        bd_letter = bd_letter.replace("[NAME]", bd_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="test@test.com",
            msg=f"Subject:Happy Birthday!\n\n{bd_letter}"
        )





