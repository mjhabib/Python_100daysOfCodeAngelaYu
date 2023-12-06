import requests

# getting info from an API endpoint
# it won't work without a VPN!
response = requests.get("http://api.open-notify.org/iss-now.json")
print(response)  # <Response [200]>
print(response.status_code)  # 200

# response codes in a glance
# 1XX = Hold on
# 2XX = Here you go
# 3XX = Go away
# 4XX = You screwed up!
# 5XX = I (server) screwed up

# now, if we didn't get a response code as we expected, the hard way is to raise an exception which is time-consuming
if response.status_code == 404:
    raise Exception("The resource does not exist! ")
elif response.status_code == 401:
    raise Exception("You are not authorised to access this data! ")

# the best way:
response.raise_for_status()

# access the API data
data = response.json()
print(f"\n {data}")

# more specific data, deal just like a dict
data = response.json()["iss_position"]
print(f"\n {data}")
data = response.json()["iss_position"]["longitude"]
print(f"\n {data}")
