class FlightData:
    def __init__(self, price, departure_city, departure_iata, destination_city, destination_iata, out_date, return_date):
        self.price = price
        self.departure_city = departure_city
        self.departure_iata = departure_iata
        self.destination_city = destination_city
        self.destination_iata = destination_iata
        self.out_date = out_date
        self.return_date = return_date


def find_cheapest_flight(data):
    quotes = data["quotes"]
    if not quotes:
        return None
    cheapest = quotes[0]
    for quote in quotes:
        if quote["price"] < cheapest["price"]:
            cheapest = quote

    # quote_request_id looks like: "ingo|10075-10957-260807|Outbound|Slc"
    parts = cheapest["quote_request_id"].split("|")
    route_and_date = parts[1]  # "10075-10957-260807"
    origin_id, destination_id, date_code = route_and_date.split("-")

    # date_code like "260807" -> YY MM DD -> convert to readable date
    out_date = f"20{date_code[0:2]}-{date_code[2:4]}-{date_code[4:6]}"

    # find matching city/airport names from data["places"] using origin_id/destination_id
    departure_city = departure_iata = destination_city = destination_iata = None
    for place in data["places"]:
        if str(place["entity_id"]) == origin_id or place.get("id") == int(origin_id):
            departure_city = place["name"]
            departure_iata = place["display_code"]
        if str(place["entity_id"]) == destination_id or place.get("id") == int(destination_id):
            destination_city = place["name"]
            destination_iata = place["display_code"]

    return FlightData(
        price=cheapest["price"],
        departure_city=departure_city,
        departure_iata=departure_iata,
        destination_city=destination_city,
        destination_iata=destination_iata,
        out_date=out_date,
        return_date=None  
    )
    
