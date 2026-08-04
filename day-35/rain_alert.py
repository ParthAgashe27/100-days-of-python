import requests
import smtplib

alerts = 4
MY_EMAIL = "your_email@gmail.com"
MY_PASSWORD = "your_password"

params = {
    "lat": "YOUR_LATITUDE",
    "lon": "YOUR_LONGITUDE",
    "appid": "YOUR_API_KEY",
    "cnt": alerts
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for i in range(0, alerts):
    id = weather_data["list"][i]["weather"][0]["id"]

    if id < 700:
        will_rain = True


with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)


    if will_rain:

        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Weather Alert!\n\nBring an umbrella. It might rain today."
            )
    else:

        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Weather Alert!\n\nNo rain today. Enjoy your day!"
            )
        
