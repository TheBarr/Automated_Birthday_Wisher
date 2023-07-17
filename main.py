import datetime as dt
import smtplib
import pandas as pd
import random

now = dt.datetime.now()
current_day = now.day
current_month = now.month

my_email = ""
password = ""

birthdays = pd.read_csv("birthdays.csv")
for index, row in birthdays.iterrows():
    if current_day == row["day"] and current_month == row["month"]:
        letter = f"letter_templates/letter_{random.randint(1, 3)}.txt"
        to_email = row["email"]
        with open(letter, "r") as letter_file:
            data = letter_file.read()
            letter_wishes = data.replace("[NAME]", row["name"])
        with smtplib.SMTP("smtp.gmail.com") as conn:
            conn.starttls()
            conn.login(my_email, password)
            conn.sendmail(
                from_addr=my_email,
                to_addrs=to_email,
                msg=f"Subject:Wishes\n\n{letter_wishes}"
            )
