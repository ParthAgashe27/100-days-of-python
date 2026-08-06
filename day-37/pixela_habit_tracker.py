import requests
from datetime import datetime

USERNAME = "YOUR_NAME"
TOKEN = "YOUR_PASSWORD"
GRAPH = "YOUR_GRAPH_NAME"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=user_params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH,
    "name": "Coding Graph",
    "unit": "commit",
    "type": "int",
    "color": "shibafu", 
}

response = requests.post(url=graph_endpoint, json=graph_config, headers={"X-USER-TOKEN": TOKEN})

post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"

today = datetime.now()


post_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": int(input("How many commits did you do today? ")),
}

response = requests.post(url=post_endpoint, json=post_config, headers={"X-USER-TOKEN": TOKEN})


update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{today.strftime('%Y%m%d')}"

update_config = {
    "quantity": int(input("Enter the new quantity: ")),
}

response = requests.put(url=update_endpoint, json=update_config, headers={"X-USER-TOKEN": TOKEN})

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{today.strftime('%Y%m%d')}"

response = requests.delete(url=delete_endpoint, headers={"X-USER-TOKEN": TOKEN})
