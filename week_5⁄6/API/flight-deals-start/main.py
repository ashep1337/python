import time
from datetime import datetime, timedelta

from data_manager import DataManager
from flight_data import find_cheapest_flight
from flight_search import FlightSearch

data_manager = DataManager()
sheet_data = data_manager.get_data()
flight_search = FlightSearch()

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_code(row["city"])

data_manager.destination_data = sheet_data
data_manager.update_data()
flight_search.get_new_token()


tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.find_prices(
        "LON", destination["iataCode"], tomorrow, six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: £{cheapest_flight.price}")
    time.sleep(2)
