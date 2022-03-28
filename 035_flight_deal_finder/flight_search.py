from flight_data import FlightData
import requests
import os


class FlightSearch:

    def __init__(self):
        self.flight_endpoint = "https://tequila-api.kiwi.com/"
        self.headers = {
            "apikey": f"{os.environ.get('API_KEY')}"
        }

    def get_destination_code(self, city_name):
        parameters = {
            "term": city_name,
            "location_types": "city"
        }

        response = requests.get(
            f"{self.flight_endpoint}/locations/query",
            params=parameters,
            headers=self.headers
        )

        data = response.json()["locations"]
        city_code = data[0]["code"]
        return city_code

    def search_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        parameters = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
            }

        response = requests.get(
            f"{self.flight_endpoint}v2/search",
            params=parameters,
            headers=self.headers
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £ {flight_data.price}")
        return flight_data
      
