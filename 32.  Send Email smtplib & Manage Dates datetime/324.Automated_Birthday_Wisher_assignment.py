import pandas
import datetime as dt
import smtplib
import random

# what day is today?
now = dt.datetime.now()
this_month = now.month
this_day = now.day

# pick a random letter
all_letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
random_letter = random.choice(all_letters)

# find a birthday that matches today
data = pandas.read_csv("birthdays.csv")
for m in data.month:
    if m == this_month:
        for d in data.day:
            if d == this_day:
                today = data[data.day == this_day]

                # change the letter's name to the birthday person
                with open(f"{random_letter}") as letter:
                    old_text = letter.read()
                    new_text = old_text.replace("[NAME]", f"{today.name.iloc[0]}")

                    # send the email
                    # with smtplib.SMTP("smtp.gmail.com") as connection:
                    #     connection.starttls()
                    #     connection.login(user="asdolacharkhi@gmail.com", password="123")
                    #     connection.sendmail(from_addr="asdolacharkhi@gmail.com",
                    #                         to_addrs=f"{today.email.iloc[0]}",
                    #                         msg=f"Subject:Hello {today.name.iloc[0]}\n\n{new_text}")

                    # printing the results instead of sending the email:
                    print(f"To: {today.email.iloc[0]}\n"
                          f"Subject: Hello {today.name.iloc[0]}\n"
                          f"Message: {new_text}")
    else:
        print("No birthday matches with today to send an email!")








