import requests
import os


class DataManager:

    def __init__(self):
        self.sheet_endpoint = os.environ.get("SHEET_ENDPOINT")
        self.headers = {
            "Authorization": f"{os.environ.get('AUTH_KEY')}"
        }
        self.destination_data = {}
        self.cities = []

    def get_destination_data(self):
        response = requests.get(
            url=f"{self.sheet_endpoint}",
            headers=self.headers
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
                url=f"{self.sheet_endpoint}/{city['id']}",
                json=new_data
            )
