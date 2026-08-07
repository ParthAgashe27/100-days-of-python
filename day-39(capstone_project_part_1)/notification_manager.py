import smtplib
class NotificationManager:
    def __init__(self):
        self.my_email = "your_email@gmail.com"  # Replace with your actual email
        self.my_password = "your_password"  # Replace with your actual email password or app password

    def send_price_alert(self, city, iata_code, price, out_date, return_date):
        message = (
            f"Subject:Low Price Alert! Flight to {city}\n\n"
            f"Only ${price} to fly from MUM to {iata_code}, "
            f"on {out_date} until {return_date}."
        )
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(self.my_email, self.my_password)
            connection.sendmail(
                from_addr=self.my_email,
                to_addrs=self.my_email,
                msg=message
            )
