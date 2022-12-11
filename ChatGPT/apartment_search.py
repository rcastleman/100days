import requests

# Set the URL for the Craigslist search
url = "https://charlottesville.craigslist.org/search/apa"

# Set the parameters for the search
params = {
    "min_price": 2500,
    "max_price": 3500,
    "availabilityMode": "0"
}

# Send the request and get the results
results = requests.get(url, params=params)

# Print the results
print(results.text)
