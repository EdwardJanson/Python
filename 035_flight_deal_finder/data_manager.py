from customer_acquisition import CustomerAcquisition
import requests
import os

SHEET_PRICES_ENDPOINT = os.environ.get("SHEET_PRICES_ENDPOINT")
SHEET_USERS_ENDPOINT = os.environ.get("SHEET_USERS_ENDPOINT")
AUTH_KEY = os.environ.get("AUTH_KEY")


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        headers = {
            "Authorization": AUTH_KEY
        }
        response = requests.get(
            url=SHEET_PRICES_ENDPOINT,
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
                url=f"{SHEET_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )

    def get_customer_emails(self):
        customers_endpoint = SHEET_USERS_ENDPOINT
        response = requests.get(url=customers_endpoint)
        data = response.json()
        customer_data = data["users"]
        return customer_data
