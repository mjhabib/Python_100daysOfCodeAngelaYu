import requests
import os
from datetime import datetime

NUTRITIONIX_API = os.environ.get("NUTRITIONIX_API_ENV")
NUTRITIONIX_ID = os.environ.get("NUTRITIONIX_ID_ENV")
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutritionix_headers = {
    "x-app-id": NUTRITIONIX_ID,
    "x-app-key": NUTRITIONIX_API,
    "x-remote-user-id": "0",
}

query = input("Which exercise you did and for how long? ")

nutritionix_json = {
    "query": query,
    # "gender":"female",
    # "weight_kg":72.5,
    # "height_cm":167.64,
    # "age":30
}

nutritionix_response = requests.post(url=NUTRITIONIX_ENDPOINT, json=nutritionix_json, headers=nutritionix_headers)
nutritionix_data = nutritionix_response.json()

SHEETY_USERNAME = os.environ.get("SHEETY_USERNAME_ENV")
SHEETY_PROJECT_NAME = os.environ.get("SHEETY_PROJECT_NAME_ENV")
SHEETY_SHEET_NAME = os.environ.get("SHEETY_SHEET_NAME_ENV")
SHEETY_ENDPOINT = "https://api.sheety.co"

SHEETY_AUTH = os.environ.get("SHEETY_AUTH_ENV")
sheety_headers = {
    "Authorization": SHEETY_AUTH
}

# add a new row to my Google sheet
counter = 0
dict_has_data = True
while dict_has_data:
    try:
        today = datetime.now()
        date = today.strftime("%d""/""%m""/""%Y")
        time = today.strftime("%H"":""%M"":""%S")
        exercise = nutritionix_data["exercises"][counter]["user_input"].title()
        duration = nutritionix_data["exercises"][counter]["duration_min"]
        calories = nutritionix_data["exercises"][counter]["nf_calories"]

        counter += 1

        nutritionix_dict = {
            "workout": {
                "date": date,
                "time": time,
                "exercise": exercise,
                "duration": duration,
                "calories": calories,
            }
        }

        sheety_response = requests.post(url=f"{SHEETY_ENDPOINT}/{SHEETY_USERNAME}/{SHEETY_PROJECT_NAME}/{SHEETY_SHEET_NAME}", json=nutritionix_dict, headers=sheety_headers)
        print(sheety_response.text)

    except:  # counter out-of-range
        dict_has_data = False
