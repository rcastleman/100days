from importlib.metadata import requires
import requests

pixela_endpoint = "https://pixe.la/v1/users"

pixela_parameters = {"token":"8cQz3q5v9L6sZ*4DXUA9XM@i#KD9@e!",
"username":"rcastleman",
"areeTermsOfService":"yes",
"notMinor":"yes"}

response = requests.post(pixela_endpoint,pixela_parameters)
