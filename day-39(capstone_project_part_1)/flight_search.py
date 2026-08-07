import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.flightapi_endpoint = "https://api.flightapi.io/roundtrip"
        self.flightapi_apikey = "FLIGHTAPI_KEY"  # Replace with your actual Flight API key

    def search_flights(self, destination, date_from, date_to):
        url = (
        f"{self.flightapi_endpoint}/{self.flightapi_apikey}/"
        f"BOM/{destination}/{date_from}/{date_to}/1/0/0/Economy/INR"
        )
        response = requests.get(url=url)
        response.raise_for_status()
        return response.json()

if __name__ == "__main__":
    flight_search = FlightSearch()
    result = flight_search.search_flights("DEL", "2026-08-07", "2027-02-16")
    print(result)
