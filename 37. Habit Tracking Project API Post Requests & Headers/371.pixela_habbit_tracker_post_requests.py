import requests

# Documentation: https://docs.pixe.la/
# Oops, it was not free to use!

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = "sdf655gsd5fg56sdf6g4sdf6g4sdf6g4sd6g"  # random-generated
USERNAME = "mjhabib"
GRAPH_ID = "graph1"

headers = {
    "X-USER-TOKEN": TOKEN
}


# create a user and see if it was successful (one-time only):

# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
# user_response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(user_response.text)


# create a graph (one-time only):

# graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
# graph_params = {
#     "id": GRAPH_ID,
#     "name": "Python Practice",
#     "unit": "H",  # as hours
#     "type": "float",
#     "color": "ajisai",  # purple
# }
# graph_response = requests.post(graph_endpoint, json=graph_params, headers=headers)
# print(graph_response.text)
# for security reasons we're going to send our token as a header not as a parameter


# Add a new pixel to my pixela python-practice tracker

pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
choice = input("Type '1' to create a new pixel, or '2' to update, or '3' to delete a previews record: ")

if choice == "1":
    date = input("Enter a date (ex: 20230718): ")
    quantity = input("How many hours did you practice Python? ")
    pixel_response = requests.post(url=pixel_endpoint, headers=headers, json={"date": date, "quantity": quantity})
    print(f"\n" + pixel_response.text)

elif choice == "2":
    date = input("Enter an old date to update (ex: 20230717): ")
    quantity = input("How many hours did you practice Python? ")
    pixel_response = requests.put(url=f"{pixel_endpoint}/{date}", headers=headers, json={"quantity": quantity})
    print(f"\n" + pixel_response.text)

elif choice == "3":
    date = input("Enter an old date to delete (ex: 20230717): ")
    pixel_response = requests.delete(url=f"{pixel_endpoint}/{date}", headers=headers)
    print(f"\n" + pixel_response.text)

else:
    exit()

# I can have access to my graph via this link:
# https://pixe.la/v1/users/mjhabib/graphs/graph1.html

# Python Date Formatting with strftime()
# https://www.w3schools.com/python/python_datetime.asp


