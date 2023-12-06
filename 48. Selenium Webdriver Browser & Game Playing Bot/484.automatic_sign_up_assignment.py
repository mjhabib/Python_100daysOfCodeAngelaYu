import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

target_url = "https://www.softgozar.com/register"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get(target_url)

name = driver.find_element(By.NAME, "ctl00$cphMaster$txtName")
name.send_keys("thisismyname")
family = driver.find_element(By.NAME, "ctl00$cphMaster$txtFamily")
family.send_keys("thisismyfamilyname")
mobile = driver.find_element(By.NAME, "ctl00$cphMaster$txtMobile")
mobile.send_keys("09123456789")
email = driver.find_element(By.NAME, "ctl00$cphMaster$txtEmail")
email.send_keys("testhi@bye.com")
username = driver.find_element(By.NAME, "ctl00$cphMaster$txtRUserName")
username.send_keys("testhibye")
passwd = driver.find_element(By.NAME, "ctl00$cphMaster$txtRPassword")
passwd.send_keys("12345abcd745@!")
passwd_confirm = driver.find_element(By.NAME, "ctl00$cphMaster$txtConfirmPassword")
passwd_confirm.send_keys("12345abcd745@!")
submit_btn = driver.find_element(By.NAME, "ctl00$cphMaster$btnRegister")
submit_btn.click()
# or - > submit_btn.send_keys(Keys.ENTER)





