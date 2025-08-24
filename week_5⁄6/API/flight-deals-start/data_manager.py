import os

import requests
from dotenv import load_dotenv


class DataManager:
    def __init__(self):
        load_dotenv("/home/ashep/Documents/Discord_bot_creds.env")

        self.SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")

        self.sheety_headers = {
            "Content-Type": "application/json",
            "Authorization": self.SHEETY_TOKEN,
        }

    def get_data(self):
        sheety_get = requests.get(
            url="https://api.sheety.co/81cd9af722a7384787d50596f1cdd719/flightDeals/prices",
            headers=self.sheety_headers,
        )

        data = sheety_get.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_data(self):
        for column in self.destination_data:
            column_id = column["id"]

            test = {"price": {"iataCode": column["iataCode"]}}

            sheety_put = requests.put(
                url=f"https://api.sheety.co/81cd9af722a7384787d50596f1cdd719/flightDeals/prices/{
                    column_id
                }",
                headers=self.sheety_headers,
                json=test,
            )
