import smtplib
import datetime as dt
import random

my_email = "beknazar.ulanbekuuluu@mail.ru"
password = "DGjDj2QjrUDdxnGDabg3"

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with open("quotes.txt") as quotes_file:
        quotes = quotes_file.readlines()
        quote = random.choice(quotes)

    with smtplib.SMTP("smtp.mail.ru") as connection:
        # secure our connection to email server
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="680633@gmail.com",
            msg=f"Subject:Motivation\n\n {quote}"
        )

# print(random.choice(quotes))

date_of_birth = dt.datetime(year=2000, month=5, day=1)
print(date_of_birth)
