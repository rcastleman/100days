from importlib.metadata import requires
from urllib import request
import requests
import secrets
from datetime import datetime


USERNAME = "rcastleman"
TOKEN = secrets.PIX_KEY
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

pixela_parameters = {"token":TOKEN,
"username":USERNAME,
"agreeTermsOfService":"yes",
"notMinor":"yes"}

# response = requests.post(url=pixela_endpoint,json=pixela_parameters)
# print(response.text)

pixela_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":GRAPH_ID,
    "name":"Coding Graph",
    "unit":"days",
    "type":"int",
    "color":"sora",
    }

headers = {
    "X-USER-TOKEN":TOKEN
}

# response = requests.post(url=pixela_graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

pixela_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

print(today.strftime("%Y%m%d"))

post_config = {
    "date":today.strftime("%Y%m%d"),
    "quantity":"1"}

# response = requests.post(
#     url=pixela_post_endpoint,
#     json=post_config,
#     headers=headers)
# print(response.text)
