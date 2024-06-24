import datetime as dt
import smtplib
import pandas
import random

email = ""
gmail_password = ""


def send_message(email_addr, message):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=email, password=gmail_password)
        connection.sendmail(
            from_addr=email,
            to_addrs=f"{email_addr}",
            msg=f"Subject:Happy Birthday\n\n{message}"
        )


now = dt.datetime.now()
today_tuple = (now.month, now.day)
placeholder = '[NAME]'

data = pandas.read_csv("./birthdays.csv")

birthday_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthday_dict:
    to_name = birthday_dict[today_tuple].loc['name']
    to_address = birthday_dict[today_tuple].loc['email']
    num = random.randint(1, 3)

    with open(f'./letter_templates/letter_{num}.txt', mode='r') as letter:
        content = letter.read()
        content = content.replace(placeholder, to_name)

    send_message(to_address, content)
