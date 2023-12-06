import requests
import os  # to set env variables
from twilio.rest import Client

weather_params = {
    "lat": 32.627161,
    "lon": 51.366389,
    "appid": os.environ.get("OWM_APPID_ENV"),
    "units": "imperial",
}

account_sid = os.environ.get("ACC_SID_ENV")
auth_token = os.environ.get("AUTH_TOKEN_ENV")


# I don't have access to the one-hour forecasts because I have a free account
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=weather_params)
response.raise_for_status()
hourly_weather = response.json()
# three-hour data in the next five-days


def rain_alert(wid):
    # it seems the system can't send SMS to my location!
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="+15737312402",
        body=f"It's going to rain today ☔ Bring an umbrella. Code: {wid}",
        to="+989374753004"
    )
    print(message.status)


# print(hourly_3_in_5_days["list"][0]["weather"][0]["id"])
counter = 4
list_goes_on = True
while list_goes_on:  # read the next 12-hour data
    weather_id = hourly_weather["list"][counter]["weather"][0]["id"]
    counter -= 1
    if 700 > weather_id >= 500:  # 5XX = rain and 6XX = snow
        rain_alert(weather_id)
        list_goes_on = False
    if counter == 0:
        list_goes_on = False
        print(f"You don't need an umbrella, id: {weather_id}")

print("\n")
print(os.environ["OWM_APPID_ENV"])

# "Environment Variables" for security & convenient reasons like not messing with the codes

# this is how we can set environment variables in PyCharm
# Open the Run Configuration selector in the top-right and click Edit Configurations...
# Select the correct file from the menu, find Environmental variables and click ...
# Add or change variables, then click OK
