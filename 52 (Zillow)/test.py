from bs4 import BeautifulSoup
import requests

URL = 'file:///Users/randycastleman/Dropbox/Mac/Documents/local_code/100_days/52%20(Zillow)/test.html'
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response = requests.get(URL)
site_data = response.text
soup = BeautifulSoup(site_data,"html.parser")

print(soup.prettify())