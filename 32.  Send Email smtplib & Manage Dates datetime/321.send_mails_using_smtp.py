import smtplib

asdola_mail = "asdolacharkhi@gmail.com"
passwd = "test123"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=asdola_mail, password=passwd)
connection.sendmail(from_addr=asdola_mail,
                    to_addrs="test@yahoo.com",
                    msg="Subject:Hello\n\nWhat's up?")
connection.close()

# or to not use close()
# with smtplib.SMTP("smtp.live.com") as connection  # "smtp.mail.yahoo.com"
#     pass


