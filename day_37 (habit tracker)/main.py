from importlib.metadata import requires
import requests
import secrets


pixela_endpoint = "https://pixe.la/v1/users"

pixela_parameters = {"token":secrets.PIX_KEY,
"username":"rcastleman",
"areeTermsOfService":"yes",
"notMinor":"yes"}

response = requests.post(pixela_endpoint,pixela_parameters)
