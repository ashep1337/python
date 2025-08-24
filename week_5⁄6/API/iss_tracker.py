import smtplib
import time
from datetime import datetime, timezone

import requests

LAT = 42.463249
LONG = -92.272079


response = requests.get(url="http://api.open-notify.org/iss-now.json")
data = response.json()
longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])
iss_position = (longitude, latitude)

parameters = {
    "lat": LAT,
    "lng": LONG,
    "formatted": 0,
}

response_sunset = requests.get(
    url="https://api.sunrise-sunset.org/json", params=parameters
)
response_sunset.raise_for_status()
data_sun = response_sunset.json()
sunrise = int(data_sun["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data_sun["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now(timezone.utc)

while True:
    time.sleep(60)
    if LAT - 5 <= latitude <= LAT + 5 and LONG - 5 <= longitude <= LONG + 5:
        if sunrise > time_now.hour > sunset:
            my_email = "jimstacy768@gmail.com"
            password = "uldk dqmc plyl acnn"

            connection = smtplib.SMTP("smtp.gmail.com", 587)
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="jimstacy768@yahoo.com",
                msg="Subject:The ISS is overhead!!!.\n\nYou better go outside and look.",
            )
            connection.close()
            print("Email sent: The ISS is overhead")
    else:
        print("The ISS is not overhead")
