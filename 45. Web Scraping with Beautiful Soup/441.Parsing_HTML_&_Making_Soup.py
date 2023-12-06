from bs4 import BeautifulSoup

with open("./441.Parsing_HTML_&_Making_Soup.html", encoding="utf-8") as html_file:
    content = html_file.read()
    # "utf-8" to solve this error: UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 278: character maps to <undefined>

soup = BeautifulSoup(content, "html.parser")
# note: in certain cases, I might want to use "lxml" as parser and I need to import it

# print(soup.prettify())  # whole website with indented tags
print(soup.title)  # <title>Angela's Personal Site</title>
print(soup.title.name)  # title
print(soup.title.string)  # Angela's Personal Site
print(soup.a)  # first anchor tag  -> <a href="https://www.appbrewery.co/">The App Brewery</a>

all_anchor_tags = soup.findAll(name="a")
print(all_anchor_tags)  # all anchor tags

for text in all_anchor_tags:
    print(text.getText())  # only texts in all anchor tags

for href in all_anchor_tags:
    print(href.get("href"))  # only links in all anchor tags

print(soup.find(name="h1", id="name"))  # find a specific id -> <h1 id="name">Angela Yu</h1>

print(soup.find(name="h3", class_="heading"))  # specific class -> <h3 class="heading">Books and Teaching</h3>
# note: since the "class" name is special to python for creating a class, we need to differentiate it with a "_" so it understands we're not looking to create a class here

company_name = soup.select_one(selector="p a")
# we're looking for the first company name, which is inside a paragraph, just like using CSS to select a specific tag
print(company_name.getText())  # The App Brewery

print(soup.select(
    selector=".heading"))  # [<h3 class="heading">Books and Teaching</h3>, <h3 class="heading">Other Pages</h3>]
# all html classes which have a ".heading" name
