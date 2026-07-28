import smtplib
import datetime as dt
import random

now = dt.datetime.now()
day_of_week = now.weekday()


my_email = "lightshadow2701@gmail.com"
password = "wnccdkoxaoccnzcw"

if day_of_week == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="lightshadow32@yahoo.com", 
            msg=f"Subject:Quote Of The Day\n\n{quote}"
        )
    connection.close()

