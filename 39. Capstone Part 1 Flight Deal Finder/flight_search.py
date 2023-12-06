from datetime import datetime
from datetime import timedelta
import pandas
import requests
import os

flight_search_data = []


class FlightSearch:
    """I'm using this Class to search through all the provided cities in "flight_deals.csv" and with the help of "KIWI API" find any number of flights in a desired range of date"""
    def __init__(self):
        self.date_from = self.tomorrow()
        self.date_to = self.date_next_six_month()
        self.fly_to()

    def tomorrow(self):
        today = datetime.now()
        tomorrow = today + timedelta(days=1)
        return tomorrow.strftime("%d""/""%m""/""%Y")

    def date_next_six_month(self):
        today = datetime.now()
        next_six_month = today + timedelta(days=90)  # 6 months = 180 days
        return next_six_month.strftime("%d""/""%m""/""%Y")

    def kiwi_search(self, city):
        kiwi_api = os.environ.get("KIWI_API_ENV")
        kiwi_endpoint = "https://api.tequila.kiwi.com/v2/search"

        kiwi_params = {
            "fly_from": "IST",  # Istanbul
            "fly_to": city,  # "PAR, BER, HND, SYD, AYT, KUL, NYC, SFO, CPT"
            "date_from": self.date_from,
            "date_to": self.date_to,
            "curr": "USD",
            "limit": 500,  # to generate less data for readability and response time
        }

        kiwi_headers = {
            "apikey": kiwi_api,
        }

        kiwi_response = requests.get(url=kiwi_endpoint, params=kiwi_params, headers=kiwi_headers)
        kiwi_response.raise_for_status()
        flight_search_data.append(kiwi_response.json())

    def fly_to(self):
        data = pandas.read_csv("flight_deals.csv")
        for city in data["IATA Code"]:
            self.kiwi_search(city)

    def return_data(self):
        return flight_search_data
