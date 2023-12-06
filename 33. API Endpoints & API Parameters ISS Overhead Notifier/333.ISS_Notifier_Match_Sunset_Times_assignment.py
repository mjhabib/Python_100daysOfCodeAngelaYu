import requests
import time
from datetime import datetime


# -------------------- Get sunrise and sunset of my location -----------------------------#

# getting an API response with specific parameters
MY_LAT = 32.619928
MY_LNG = 51.374456
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

sun_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
# or  -  https://api.sunrise-sunset.org/json?lat=32.619928&lng=51.374456
sun_response.raise_for_status()

data = sun_response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
# print(sunrise.split("T")[1].split(":")[0])  # 01
# 2023-07-15T01:36:09+00:00  -  ['2023-07-15', '01:36:09+00:00']  -  ['01', '36', '09+00', '00']

sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
# print(sunset)  # 15

# -------------------- Get local time in this moment -----------------------------#

time_now = datetime.now().hour
# print(time_now.hour)  # 23
minute_now = datetime.now().minute


# -------------------- Get ISS location coordinates -----------------------------#

iss_response = requests.get("http://api.open-notify.org/iss-now.json")
iss_response.raise_for_status()
iss_data = iss_response.json()
iss_long = float(iss_data["iss_position"]["longitude"])
iss_lat = float(iss_data["iss_position"]["latitude"])

# -------------------- Check every 60 seconds if ISS close to me and it's dark -----------------------------#

while True:
    time.sleep(60)
    if sunset > time_now < sunrise and MY_LNG + 5 < iss_long > MY_LNG - 5 and MY_LAT + 5 < iss_lat > MY_LAT - 5:
        # 20 > 18 < 05 and 56 < 40 > 46 and 37 < 30 > 47
        print("send an email notifier!")  # I'm not going to write the codes related to sending an email
