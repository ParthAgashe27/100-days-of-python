from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

my_email = os.environ.get("EMAIL_ADDRESS")
my_password = os.environ.get("EMAIL_PASSWORD")


URL = "https://appbrewery.github.io/instant_pot/"

response = requests.get(URL)

soup = BeautifulSoup(response.content, "html.parser")
BUY_PRICE = 100.0

price = float(soup.find(name="span", class_="aok-offscreen").getText().split("$")[1])
name = soup.find(name="span", class_="a-size-large product-title-word-break").getText()

if price < BUY_PRICE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
        from_addr=my_email,
        to_addrs=my_email,
        msg=f"Subject:Price Alert\n\n{name} is now ${price}".encode("utf-8")
    )


