from importlib.metadata import requires
from urllib import request
import requests
import secrets
from datetime import datetime


#----------------------- variables ------------------------#

USERNAME = "rcastleman"
TOKEN = secrets.PIX_KEY
GRAPH_ID = "graph1"


#----------------------- set up account ---------------------#

pixela_endpoint = "https://pixe.la/v1/users"

pixela_parameters = {"token":TOKEN,
"username":USERNAME,
"agreeTermsOfService":"yes",
"notMinor":"yes"}

# response = requests.post(url=pixela_endpoint,json=pixela_parameters)
# print(response.text)

#----------------------- set up graph ------------------------#

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


#----------------------- post to  graph --------------------------#


pixela_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

#trying out date formatting to make posting easier
# print(today.strftime("%Y%m%d"))

post_config = {
    "date":today.strftime("%Y%m%d"),
    "quantity":"1"}

response = requests.post(
    url=pixela_post_endpoint,
    json=post_config,
    headers=headers)
print(response.text)

# graph at https://pixe.la/v1/users/rcastleman/graphs/graph1


#------------------------ Put (update) a pixel ------------------ #

date = "2202-09-12"
quantity = 2

pixela_put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"

put_config = {"quantity":quantity}

response = requests.put(
    url=pixela_put_endpoint,
    json = put_config,
    headers = headers)