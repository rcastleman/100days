from importlib.metadata import requires
from urllib import request
import requests
import secrets

USERNAME = "rcastleman"
TOKEN = secrets.PIX_KEY

pixela_endpoint = "https://pixe.la/v1/users"

pixela_parameters = {"token":TOKEN,
"username":USERNAME,
"agreeTermsOfService":"yes",
"notMinor":"yes"}

# response = requests.post(url=pixela_endpoint,json=pixela_parameters)
# print(response.text)

pixela_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":"graph1",
    "name":"Coding Graph",
    "unit":"days",
    "color":"sora",
    }

response = requests.push(url=pixela_graph_endpoint)
