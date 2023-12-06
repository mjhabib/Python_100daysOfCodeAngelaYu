from selenium import webdriver
from selenium.webdriver.common.by import By

# Perhaps before running the code below, I need to set up my chrome driver's path using Windows terminal like this:
# setx path "%path%;D:\Software\chromedriver\chromedriver.exe"

amz_driver = webdriver.Chrome()
amz_driver.get(
    "https://www.amazon.com/Apple-MU8F2AM-A-Pencil-Generation/dp/B07K1WWBJK/ref=lp_16225009011_1_3?sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D")
amz_price = amz_driver.find_element(By.ID, "price_inside_buybox")
# By.CLASS_NAME - By.CSS_SELECTOR - By.TAG_NAME - etc...
print(amz_price.text)  # $89.00

amz_driver.quit()

# the primary difference between Selenium and BS6 is, since this method drives (opens up) a browser, it renders all the elements of the page like its javascript as is a human interacts with that website, and the results are more likely better. Also, it has more features.

# --------------- *** -------------------------

py_driver = webdriver.Chrome()
py_driver.get("https://www.python.org/")
py_search_bar = py_driver.find_element(By.NAME, "q")

print(py_search_bar.tag_name)  # input
print(py_search_bar.get_attribute("placeholder"))  # Search

py_a_tag = py_driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# for items that we can't easily access to, first we found the class name of a "div" which contains an "a-href tag" and printed out its text
# note: our class name starts with "." and we must eliminate words which has spaces
print(py_a_tag.text)  # docs.python.org

py_xpath = py_driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# by right-click on that element, we can copy it's Xpath
print(py_xpath.text)  # Submit Website Bug

py_driver.quit()
