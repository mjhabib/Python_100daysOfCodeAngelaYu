from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

target_url = ("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location"
"=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
user = "asdolacharkhi@gmail.com"
passwd = "A:3VWSG*#T*gi+UA"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get(target_url)

sign_in = driver.find_element(By.CSS_SELECTOR, 'a[href="https://www.linkedin.com/login?emailAddress=&fromSignIn=&fromSignIn=true&session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fjobs%2Fsearch%2F%3Ff_LF%3Df_AL%26geoId%3D102257491%26keywords%3Dpython%2520developer%26location%3DLondon%252C%2520England%252C%2520United%2520Kingdom%26redirect%3Dfalse%26position%3D1%26pageNum%3D0&trk=public_jobs_nav-header-signin"]')
sign_in.click()

username = driver.find_element(By.ID, "username")
username.send_keys(user)
password = driver.find_element(By.ID, "password")
password.send_keys(passwd)
submit_btn = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
submit_btn.click()

# and the rest is history ...

