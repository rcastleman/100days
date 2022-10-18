import requests
from bs4 import BeautifulSoup



# user_date = input("Year? (YEAR-MO-DATE): ")

# URL = f"https://www.billboard.com/charts/hot-100/{user_date}"

# print(URL)

# response = requests.get(URL)
response = requests.get("https://www.billboard.com/charts/hot-100/2000-08-12/")
website_html = response.text
soup = BeautifulSoup(website_html,"html.parser")

print(soup.prettify())

all_songs = soup.find_all(name="h3",class_="c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")

titles = [song.getText() for song in all_songs]

# print(titles)

# with open("songs.txt",mode="w") as file:
#     for song in titles:
#         file.write(f"{song}\n")