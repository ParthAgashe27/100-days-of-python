import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):

        self.sheety_endpoint = "SHEETY_ENDPOINT"  # Replace with your actual Sheety endpoint
        self.sheety_headers = {
            "Authorization": "SHEETY_KEY"  # Replace with your actual Sheety API key
        }
    def get_sheet_data(self):
        response = requests.get(self.sheety_endpoint, headers=self.sheety_headers)
        response.raise_for_status()
        self.destination_data = response.json()["prices"]  # adjust key to match your sheet name
        return self.destination_data

    def update_price(self, row_id, new_price):
        update_endpoint = f"{self.sheety_endpoint}/{row_id}"
        payload = {
            "price": {
                "lowestPrice": new_price
            }
        }
        response = requests.put(update_endpoint, json=payload, headers=self.sheety_headers)
        response.raise_for_status()
        return response.json()
