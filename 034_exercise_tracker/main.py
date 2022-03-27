import requests
import os
from datetime import datetime

APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")
SHEET_KEY = os.environ.get("SHEET_KEY")
app_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ.get("SHEET_ENDPOINT")

GENDER = # gender
WEIGHT = # weight in kg
HEIGHT_CM = # height in cm
AGE = # your age

exercise_input = input("What exercise did you do today? ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "Authorization": SHEET_KEY
}

exercise_params = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

exercise_response = requests.post(url=app_endpoint, json=exercise_params, headers=headers)
exercise_data = exercise_response.json()["exercises"]

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in exercise_data:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=headers)
