# #################### Normal Starting Project ######################
from datetime import datetime
import pandas, random, smtplib

MY_EMAIL = "beknazar.ulanbekuuluu@mail.ru"
password = "Uzsk7NVgAAdbAGw1v06E"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

# HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
if today_tuple in birthdays_dict:
    birthdays_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthdays_person['name'])

    with smtplib.SMTP("smtp.mail.ru") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=password)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthdays_person['email'],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )

# This project includes:
# Dictionary comprehensions
# Reading Comma separated values (csv)
# Creating DataFrames from pandas
# Using and creating tuples
# Working with dictionaries, file path
# Opening file, replacing files, reading them
# Writing and sending emails as well as datatime module
