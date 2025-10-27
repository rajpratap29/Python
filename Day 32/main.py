# import smtplib

# my_email = "glitchfox.in@gmail.com"
# password = "add your app password here"

# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="kingsmen00000@gmail.com", 
#         msg="Subject:Hello\n\nThis is body of email."
#     )


# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
# date_of_birth = dt.datetime(year=2005, month=1, day=29)


import smtplib
import datetime as dt
import random

MY_EMAIL = "glitchfox.in@gmail.com"
MY_PASSWORD = "add your app password here"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("Day 32/quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)

    print(quote) 
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )