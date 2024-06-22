# #################### Hard Starting Project ######################
import pandas, smtplib, random, os
import datetime as dt
PLACEHOLDER = "[NAME]"

my_email = "beknazar.ulanbekuuluu@mail.ru"
password = "Uzsk7NVgAAdbAGw1v06E"

data = pandas.read_csv("birthdays.csv")
data_rows = data.to_dict(orient="record")
birthdays_dict = {(item['month'], item['day']): item for item in data_rows}

today = dt.datetime.today()
today_tuple = (today.month, today.day)

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    random_file = random.choice(os.listdir("letter_templates/"))
    with open(f"letter_templates/{random_file}") as random_letter_file:
        letter = random_letter_file.read()
        new_letter = letter.replace(PLACEHOLDER, birthday_person['name'])

    with smtplib.SMTP("smtp.mail.ru") as connection:
        # secure our connection to email server
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person['email'],
            msg=f"Subject:Happy Birthday!\n\n{new_letter}"
        )
