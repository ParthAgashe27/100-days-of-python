import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.flightapi_roundtrip_endpoint = "https://api.flightapi.io/roundtrip"
        self.flightapi_multitrip_endpoint = "https://api.flightapi.io/multitrip"
        self.flightapi_apikey = "YOUR_FLIGHT_API_KEY"  # Replace with your actual Flight API key
        
        self.trips = "3"

    def search_flights(self, destination, date_from, date_to):
        url = (
        f"{self.flightapi_roundtrip_endpoint}/{self.flightapi_apikey}/"
        f"BOM/{destination}/{date_from}/{date_to}/1/0/0/Economy/INR"
        )
        response = requests.get(url=url)
        if response.status_code != 200:
            print("ERROR BODY:", response.text)
        response.raise_for_status()
        return response.json()


    # def search_multi_city_flights(self, legs, adults=1, children=0, infants=0, cabinclass="Economy", currency="INR"):
    #     params = {
    #         "adults": str(adults),
    #         "children": str(children),
    #         "infants": str(infants),
    #         "cabinclass": cabinclass,
    #         "currency": currency,
    #         "trips": str(len(legs))
    #     }

    #     for i, (departure, arrival, date) in enumerate(legs, start=1):
    #         params[f"arp{2*i - 1}"] = departure
    #         params[f"arp{2*i}"] = arrival
    #         params[f"date{i}"] = date

    #     url = f"{self.flightapi_multitrip_endpoint}/{self.flightapi_apikey}"
    #     response = requests.get(url, params=params)
    #     response.raise_for_status()
    #     return response.json()
        

if __name__ == "__main__":
    flight_search = FlightSearch()
    rt_result = flight_search.search_flights("DEL", "2026-09-01", "2027-02-16")
    print(rt_result)


    # multi_result = flight_search.search_multi_city_flights([
    #     ("BOM", "GOI", "2026-09-15"),
    #     ("GOI", "BOM", "2026-09-20")
    # ])
    # print("MULTITRIP RESULT:", multi_result)
