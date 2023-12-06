import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()
ycombinator = response.text

soup = BeautifulSoup(ycombinator, "html.parser")
all_headlines = soup.find_all(name="span", class_="titleline")

titles = []
for title in all_headlines:
    titles.append(title.getText())

links = []
all_a_tags = soup.find_all(name="a", rel="noreferrer")
for link in all_a_tags:
    links.append(link.get("href"))

all_scores = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

highest_score = all_scores.index(max(all_scores))

print(f"Check-out: {titles[highest_score]}\n Here: {links[highest_score]}")
