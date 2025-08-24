import datetime as dt
import random
import smtplib

now = dt.datetime.now()
day = now.weekday()

if day == 4:
    quotes_list = []
    with open("quotes.txt", "r") as file:
        for line in file:
            quotes_list.append(line)

    pick_quote = random.choice(quotes_list)
    my_email = "jimstacy768@gmail.com"
    password = "uldk dqmc plyl acnn"

    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="jimstacy768@yahoo.com",
        msg=f"Subject:Quote of the day.\n\n{pick_quote}",
    )
    connection.close()

    print("Email sent")
else:
    print("Email not sent")

print(pick_quote)
# my_email = "jimstacy768@gmail.com"
# password = "uldk dqmc plyl acnn"
#
# connection = smtplib.SMTP("smtp.gmail.com", 587)
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(
#   from_addr=my_email,
#   to_addrs="jimstacy768@yahoo.com",
#   msg="Subject:Hello World\n\nThis is a test. Hello World!",
# )
# connection.close()

#
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
#
# birthday = dt.datetime(year=1994, month=6, day=20)
#
# print(dt.datetime.now())
# print(birthday)
