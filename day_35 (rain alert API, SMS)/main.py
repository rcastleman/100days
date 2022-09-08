
# https://home.openweathermap.org/api_keys

API_KEY = "8f21e2683deb718640c8241bb5e63746"

NYC_LAT = 40.753270
NYC_LNG = -73.971660

API_URL = f"https://api.openweathermap.org/data/2.5/weather?lat={NYC_LAT}&lon={NYC_LNG}&appid={API_KEY}&units=imperial"

print(API_URL)

