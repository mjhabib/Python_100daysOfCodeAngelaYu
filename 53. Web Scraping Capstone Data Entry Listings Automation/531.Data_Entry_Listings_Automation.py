import requests
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

TARGET_URL = "https://www.zillow.com"
CITY = "vancouver-bc"
GOAL = "rentals"
SEARCH_FILTERS = 'searchQueryState=%7B"pagination"%3A%7B%7D%2C"usersSearchTerm"%3A"Vancouver%20BC"%2C"mapBounds"%3A%7B"west"%3A-123.23515889501954%2C"east"%3A-123.02367207861329%2C"south"%3A49.194418942551955%2C"north"%3A49.3010987914176%7D%2C"mapZoom"%3A12%2C"regionSelection"%3A%5B%7B"regionId"%3A791534%2C"regionType"%3A6%7D%5D%2C"isMapVisible"%3Atrue%2C"filterState"%3A%7B"price"%3A%7B"max"%3A780629%7D%2C"beds"%3A%7B"min"%3A1%7D%2C"con"%3A%7B"value"%3Afalse%7D%2C"fore"%3A%7B"value"%3Afalse%7D%2C"apa"%3A%7B"value"%3Afalse%7D%2C"mp"%3A%7B"max"%3A4000%7D%2C"ah"%3A%7B"value"%3Atrue%7D%2C"auc"%3A%7B"value"%3Afalse%7D%2C"nc"%3A%7B"value"%3Afalse%7D%2C"fr"%3A%7B"value"%3Atrue%7D%2C"tow"%3A%7B"value"%3Afalse%7D%2C"fsbo"%3A%7B"value"%3Afalse%7D%2C"cmsn"%3A%7B"value"%3Afalse%7D%2C"apco"%3A%7B"value"%3Afalse%7D%2C"fsba"%3A%7B"value"%3Afalse%7D%7D%2C"isListVisible"%3Atrue%7D'
# upto $4K, and one bedroom, and only houses (exclude apartments)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,fa-IR;q=0.8,fa;q=0.7",
}
GOOGLE_FORM = "https://forms.gle/8DWF9wS1LnM6sGvZ6"


class DataEntry:
    def __init__(self):
        # requests setup
        response = requests.get(url=f"{TARGET_URL}/{CITY}/{GOAL}/?{SEARCH_FILTERS}", headers=HEADERS)
        response.raise_for_status()
        raw_data = response.text

        # beautiful-soup setup
        self.soup = BeautifulSoup(raw_data, "lxml")

        # selenium setup
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)

    def extract_data_from_soup(self):
        all_links = self.soup.find_all(name="a", class_="StyledPropertyCardDataArea-c11n-8-84-3__sc-yipmu-0 jnnxAW property-card-link")
        self.links_list = [link.get("href") for link in all_links]

        all_prices = self.soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1 iMKTKr")
        self.prices_list = [price.text.strip("C/mo") for price in all_prices]

        all_addresses = self.soup.find_all(name="a", class_="StyledPropertyCardDataArea-c11n-8-84-3__sc-yipmu-0 jnnxAW property-card-link")
        self.addresses_list = [address.text for address in all_addresses]

    def save_data_into_form(self):
        counter = 0
        self.driver.get(GOOGLE_FORM)
        time.sleep(3)

        for _ in range(len(self.addresses_list)):
            all_elements = self.driver.find_elements(By.CSS_SELECTOR, ".rFrNMe input")

            address = all_elements[0]
            address.send_keys(self.addresses_list[counter])
            time.sleep(1)

            price = all_elements[1]
            price.send_keys(self.prices_list[counter])
            time.sleep(1)

            link = all_elements[2]
            link.send_keys(self.links_list[counter])
            time.sleep(1)

            submit = self.driver.find_element(By.CSS_SELECTOR, ".ThHDze span")
            submit.click()
            time.sleep(3)

            next_form = self.driver.find_element(By.CSS_SELECTOR, ".c2gzEf a")
            next_form.click()
            time.sleep(5)
            counter += 1


run_program = DataEntry()
run_program.extract_data_from_soup()
run_program.save_data_into_form()


