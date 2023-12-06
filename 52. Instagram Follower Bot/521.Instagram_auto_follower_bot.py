import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

IG_USER = "ministry_of_freedom"
IG_PSS = "ZqYA9L38XbVHSRr"  # removed double-auth
USER_TARGET = "leomessi"
target_url = f"https://www.instagram.com"


class InstaFollower:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(target_url)
        time.sleep(3)

    def login(self):
        username = self.driver.find_element(By.NAME, "username")
        passwd = self.driver.find_element(By.NAME, "password")
        username.send_keys(IG_USER)
        passwd.send_keys(IG_PSS)
        time.sleep(5)
        passwd.send_keys(Keys.ENTER)
        # or:
        # log_in = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')
        # log_in.click()
        time.sleep(5)

    def followers(self):
        # Goto to the Messi followers page
        self.driver.get(f"https://www.instagram.com/{USER_TARGET}/followers")
        time.sleep(10)

        # scroll down
        follower_pop_up = self.driver.find_element(By.CSS_SELECTOR, '.x9f619 ._aano')
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follower_pop_up)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CLASS_NAME, "_acan")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower()
bot.login()
bot.followers()
bot.follow()
