import os
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv("/home/ashep/Documents/Discord_bot_creds.env")

APP_ID = "1df65ac5"
API_KEY = "6a5d34f82e14c4790d37479d397ffd27"
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")

today = datetime.now()
today_formatted = today.strftime("%m/%d/%Y")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

params = {"query": input("Provide time and type of work out: ")}

response = requests.post(
    url="https://trackapi.nutritionix.com/v2/natural/exercise",
    headers=headers,
    json=params,
)

data = response.json()
type_data = data["exercises"][0]
exercise = type_data["name"]
duration = type_data["duration_min"]
cals = type_data["nf_calories"]
time = today.strftime("%I:%M:%S")
add_row = {
    "workout": {
        "date": today_formatted,
        "time": time,
        "exercise": exercise,
        "duration": f"{duration} mins",
        "calories": cals,
    }
}

sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": SHEETY_TOKEN,
}
sheety_response = requests.post(
    url="https://api.sheety.co/81cd9af722a7384787d50596f1cdd719/100DoC/workouts",
    headers=sheety_headers,
    json=add_row,
)
print(sheety_response)
