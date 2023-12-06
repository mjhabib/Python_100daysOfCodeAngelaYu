from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.python.org/")

all_dates = driver.find_elements(By.TAG_NAME, "time")
dates_list = [date.text for date in all_dates[5::]]
# eliminate the first 5 dates which is related to the "latest news" section

all_events = driver.find_elements(By.CSS_SELECTOR, ".event-widget a")
events_list = [event.text for event in all_events[1::]]
# the first a-href was a link called "more" so I eliminate it using list slicing

events_dict = {(dates_list[i], events_list[i]) for i in range(len(dates_list))}

print(events_dict)
driver.quit()

# teacher's solution:

# all_dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# all_events = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

# events_dict = {}
# for n in range(len(all_dates)):
#     events_dict[n] = {
#         "time": all_dates[n].text,
#         "name": all_events[n].text,
#     }
