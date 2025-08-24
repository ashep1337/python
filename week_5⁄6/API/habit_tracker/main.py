from datetime import datetime

import requests

pixela_endpoint = "https://pixe.la/v1/users"

TOKEN = "123456789abcd"

user_params = {
    "token": "123456789abcd",
    "username": "ashep1337",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# created pixela graph

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = "https://pixe.la/v1/users/ashep1337/graphs"

graph_config = {
    "id": "g1",
    "name": "Coding Tracker",
    "unit": "Time",
    "type": "float",
    "color": "shibafu",
}

pixel_endpoint = "https://pixe.la/v1/users/ashep1337/graphs/g1"
update_endpoint = "https://pixe.la/v1/users/ashep1337/graphs/g1/20250817"

today = datetime.now()
today_formatted = today.strftime("%Y%m%d")

pixel_config = {
    "date": today_formatted,
    "quantity": "5",
}

headers = {"X-USER-TOKEN": TOKEN}

pixel_update = {
    "quantity": "255",
}


# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response)

# post_pixel = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)

update_pixel = requests.delete(url=update_endpoint, headers=headers)
