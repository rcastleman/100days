from bs4 import BeautifulSoup
import requests

URL = 'file:///Users/randycastleman/Dropbox/Mac/Documents/local_code/100_days/52%20(Zillow)/test.html'

headers = ''
response = requests.get(URL)
site_data = response.text
soup = BeautifulSoup(site_data,"html.parser",headers)

print(soup.prettify())