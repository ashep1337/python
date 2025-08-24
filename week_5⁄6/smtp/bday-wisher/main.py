import datetime as dt
import random
import smtplib

import pandas

files = [
    "./letter_templates/letter_1.txt",
    "./letter_templates/letter_2.txt",
    "./letter_templates/letter_3.txt",
]
date = dt.datetime.today()
month_day = date.month, date.day

data = pandas.read_csv("birthdays.csv")

data_dict = {
    (row.month, row.day): (row.names, row.email, row.year, row.month, row.day)
    for (index, row) in data.iterrows()
}

if month_day in data_dict:
    get_email = data_dict[month_day][1]
    name = data_dict[month_day][0]

    with open(random.choice(files)) as file:
        content = file.read()
        content = content.replace("[NAME]", name)
        print(content)
    my_email = "jimstacy768@gmail.com"
    password = "uldk dqmc plyl acnn"

    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=get_email,
        msg=f"Subject:Happy Birthday!\n\n{content}",
    )
    connection.close()
    print("Email Sent")
else:
    print("No birthdays todaay")
