import smtplib
import datetime as dt
import random

# pick a random quote from text
with open("quotes.txt", "r") as file:
    ran_quote = random.choice(file.readlines())

asdola_mail = "asdolacharkhi@gmail.com"
passwd = "test123"

# check the day of the week and send an email on mondays
now = dt.datetime.now()
if now.weekday() == 0:  # 0 = monday
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=asdola_mail, password=passwd)
        connection.sendmail(from_addr=asdola_mail,
                            to_addrs="test@yahoo.com",
                            msg=f"Subject:Monday Motivational Quote\n\n{ran_quote}")
