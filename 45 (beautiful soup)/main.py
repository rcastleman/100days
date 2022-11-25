from bs4 import BeautifulSoup

with open("website.html") as f:
    contents = f.read()

soup = BeautifulSoup(contents,"html.parser")

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print(soup.prettify())

print(soup.a)

all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))

# heading = soup.find(id = "name")
# print(heading)

# section_heading = soup.find(class_ = "heading")
# print(section_heading.name)
