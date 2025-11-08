import requests
from datetime import datetime

USERNAME = "rajpratap"
TOKEN = "hiufh278f283bu"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{graph_endpoint}/{graph_config['id']}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5.5",
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

pixel_update_endpoint = f"{pixel_creation_endpoint}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "10",
}

# response = requests.put(url=pixel_update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

pixel_delete_endpoint = f"{pixel_creation_endpoint}/{today.strftime('%Y%m%d')}"

response = requests.delete(url=pixel_delete_endpoint, headers=headers)
print(response.text)