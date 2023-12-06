from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


target_url = "https://orteil.dashnet.org/cookieclicker/"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get(target_url)

time.sleep(30)  # to sync my internet speed with this program
eng_lng = driver.find_element(By.ID, "langSelect-EN")
eng_lng.click()

time.sleep(30)
cookie = driver.find_element(By.ID, "bigCookie")
while True:  # unlimited loop - just to test my code
    cookie.click()

