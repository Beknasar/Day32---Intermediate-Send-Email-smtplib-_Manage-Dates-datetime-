# #################### Extra Hard Starting Project ######################
import datetime as dt
import pandas, random, os, smtplib
PLACEHOLDER = "[NAME]"

my_email = "beknazar.ulanbekuuluu@mail.ru"
password = "Uzsk7NVgAAdbAGw1v06E"

today = dt.date.today()
today_to_check = today.strftime('%m-%d')

data = pandas.read_csv("birthdays.csv")
birthday_data = data.to_dict(orient="record")

for data in birthday_data:
    birthday_string = f"{data['year']}-{data['month']}-{data['day']}"
    birthday = dt.datetime.strptime(birthday_string, "%Y-%m-%d").date()
    birthday_to_check = birthday.strftime('%m-%d')
    # 2. Check if today matches a birthday in the birthdays.csv ✅
    if today_to_check == birthday_to_check:
        # 3. If step 2 is true, pick a random letter from letter templates and
        # replace the [NAME] with the person's actual name from birthdays.csv ✅
        random_file = random.choice(os.listdir("letter_templates/"))
        with open(f"letter_templates/{random_file}") as random_letter_file:
            letter = random_letter_file.read()
            new_letter = letter.replace(PLACEHOLDER, data["name"])

        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.mail.ru") as connection:
            # secure our connection to email server
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=f"{data['email']}",
                msg=f"Subject:Happy Birthday!\n\n{new_letter}"
            )