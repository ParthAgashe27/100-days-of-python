
import smtplib
class NotificationManager:
    def __init__(self):
        self.my_email = "YOUR_MAIL@gmail.com"
        self.my_password = "PASSWORD"


    def send_price_alert(self, deals, recipient_list):
        message = "Subject:Low Price Alert!\n\n"
        for deal in deals:
            message += (
                f"Flight to {deal['city']}\n"
                f"Only ₹{deal['price']} to fly from MUM to {deal['iata_code']}, "
                f"on {deal['out_date']} until {deal['return_date']}.\n\n"
        )

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(self.my_email, self.my_password)
            for email in recipient_list:
                connection.sendmail(
                    from_addr=self.my_email,
                    to_addrs=email,
                    msg=message
                )
