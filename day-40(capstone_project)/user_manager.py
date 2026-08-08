import requests

class UserManager:
    # This class is responsible for managing user data.
    def __init__(self):
        self.sheety_endpoint_users = "YOUR_SHEETY_ENDPOINT"
        self.sheety_headers = {
            "Authorization": "YOUR_SHEETY_API_KEY"  # Replace with your actual Sheety API key
        }

    def get_user_data(self):
        response = requests.get(self.sheety_endpoint_users, headers=self.sheety_headers)
        response.raise_for_status()
        self.user_data = response.json()["users"]  # adjust key to match your sheet name
        return self.user_data

