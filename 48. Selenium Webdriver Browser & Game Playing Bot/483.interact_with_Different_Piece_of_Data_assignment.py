from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# this is how we can stop our browser from closing automatically
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
wiki_count = driver.find_element(By.CSS_SELECTOR, 'a[href="/wiki/Special:Statistics"]')  # or -> '#articlecount a'

# this is how we can click on a specific link
# wiki_count.click()

# another way for doing that:
wikipedia_page = driver.find_element(By.LINK_TEXT, "Wikipedia")
# wikipedia_page.click()

# put a text as an input into the searchbar
wiki_search = driver.find_element(By.NAME, "search")
wiki_search.send_keys("Python")  # type 'Python' into the searchbar
wiki_search.send_keys(Keys.ENTER)  # then hit 'Enter'
