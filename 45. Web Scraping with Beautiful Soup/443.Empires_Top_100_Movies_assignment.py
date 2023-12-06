import requests
from bs4 import BeautifulSoup
import lxml

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
response.raise_for_status()
movies_html = response.text

soup = BeautifulSoup(movies_html, "lxml")
titles = soup.find_all("h3", class_="title")

# text = []
# for title in titles:
#     text.append(title.getText())
text = [title.getText() for title in titles]

with open("./443.movies_list.txt", mode="w", encoding="utf-8") as file:
    for line in reversed(text):
        # loop through the list backwards --or-- text[::-1]  --or -- range(len(text) -1, -1, -1)
        file.write(f"{line}\n")
