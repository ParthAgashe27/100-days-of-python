from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from flight_data import find_cheapest_flight
from datetime import datetime, timedelta


data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_sheet_data()


tomorrow = datetime.now() + timedelta(days=1)
six_months = datetime.now() + timedelta(days=180)

date_from = tomorrow.strftime("%Y-%m-%d")
date_to = six_months.strftime("%Y-%m-%d")

for row in sheet_data:
    destination_iata = row["iataCode"]  # match your sheet's actual column name
    print(f"Checking flights to {row['city']}...")

    result = flight_search.search_flights(destination_iata, date_from, date_to)
    cheapest_flight = find_cheapest_flight(result)

    if cheapest_flight is None:
        print(f"No flights found for {row['city']}")
        continue

    print(f"{row['city']}: ₹{cheapest_flight.price}")

    if row.get("lowestPrice") is None or cheapest_flight.price < row["lowestPrice"]:        
        notification_manager.send_price_alert(
            city=row["city"],
            iata_code=cheapest_flight.destination_iata,
            price=cheapest_flight.price,
            out_date=cheapest_flight.out_date,
            return_date=cheapest_flight.return_date
        )
        data_manager.update_price(row["id"], cheapest_flight.price)
