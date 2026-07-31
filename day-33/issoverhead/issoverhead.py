import requests
from datetime import datetime
import smtplib
import time

MY_LAT = YOUR LAT # Your latitude
MY_LONG = YOUR LANG # Your longitude

MY_EMAIL = "YOUR MAIL"
MY_PASS = "YOUR PASS"

def iss_above():
    
#Your position is within +5 or -5 degrees of the ISS position.

    buffer_position_lat_plus = MY_LAT + 5 
    buffer_position_lat_minus = MY_LAT - 5
    buffer_position_long_plus = MY_LONG + 5
    buffer_position_long_minus = MY_LONG - 5
    
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if buffer_position_lat_minus <= iss_latitude <= buffer_position_lat_plus and buffer_position_long_minus <= iss_longitude <= buffer_position_long_plus:
            return True

def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
while True:
    time.sleep(60)
    if iss_above() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASS)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=f"Subject: ISS LOCATION ALERT\n\nLOOK UP ISS IS ABOVE YOU!!!"
        )





