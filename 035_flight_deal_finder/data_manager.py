import requests
import os

SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")
AUTH_KEY = os.environ.get("AUTH_KEY")


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        headers = {
            "Authorization": AUTH_KEY
        }
        response = requests.get(
            url=SHEET_ENDPOINT,
            headers=headers
        )
        self.destination_data = response.json()["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            requests.put(
                url=f"{SHEET_ENDPOINT}/{city['id']}",
                json=new_data
            )
