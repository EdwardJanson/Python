import requests
import os
from datetime import datetime


USERNAME = os.environ.get("USERNAME")
TOKEN = os.environ.get("TOKEN_KEY")
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# create account
# response = requests.post(url=pixela_endpoint, json=user_params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Hours",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# create graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

today = datetime.now()
quantity = 0

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": quantity
}

# new pixel
# response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)

updated_date = datetime(year=2022, month=3, day=26).strftime("Y%m%d")
updated_quantity = 0

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{updated_date}"

pixel_update_data = {
    "quantity": updated_quantity
}

# update pixel
# response = requests.put(url=pixel_update_endpoint, json=pixel_data, headers=headers)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{updated_date}"

# delete pixel
# response = requests.delete(url=pixel_update_endpoint, headers=headers)
