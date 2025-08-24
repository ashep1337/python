import os

import requests
from dotenv import load_dotenv


class FlightSearch:
    def __init__(self):
        load_dotenv("/home/ashep/Documents/Discord_bot_creds.env")
        self.FLIGHT_API = os.getenv("FLIGHT_API")
        self.FLIGHT_SECRET = os.getenv("FLIGHT_SECRET")

        self._token = self.get_new_token()

    def get_new_token(self):
        header = {"Content-Type": "application/x-www-form-urlencoded"}
        body = {
            "grant_type": "client_credentials",
            "client_id": self.FLIGHT_API,
            "client_secret": self.FLIGHT_SECRET,
        }

        response = requests.post(
            url="https://test.api.amadeus.com/v1/security/oauth2/token",
            headers=header,
            data=body,
        )

        return response.json()["access_token"]

    def get_code(self, city_name):
        print(self._token)
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {"keyword": city_name, "max": "2", "include": "AIRPORTS"}

        search_results = requests.get(
            url="https://test.api.amadeus.com/v1/reference-data/locations/cities",
            params=query,
            headers=headers,
        )

        code = search_results.json()["data"][0]["iataCode"]

        return code

    def find_prices(self, origin_code, destination_code, from_time, to_time):
        headers = {"Authorization": f"Bearer {self._token}"}

        query = {
            "originLocationCode": origin_code,
            "destinationLocationCode": destination_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "currencyCode": "USD",
            "adults": "1",
            "max": "5",
            "nonStop": "true",
        }

        response = requests.get(
            url="https://test.api.amadeus.com/v2/shopping/flight-offers",
            params=query,
            headers=headers,
        )

        return response.json()
