import requests
from datetime import datetime
from datetime import timedelta  # to retrieve yesterday's data

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

ALPHA_API = "6J1N2FDMD7ENFRVB"
ALPHA_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_API = "aea7ec22237a49929e7b4aa366980151"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_ENDPOINT_Top = "https://newsapi.org/v2/top-headlines"

alpha_params = {
    "apikey": ALPHA_API,
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,

}

alpha_response = requests.get(ALPHA_ENDPOINT, params=alpha_params)
alpha_response.raise_for_status()
alpha_data = alpha_response.json()

today = datetime.now().date()
weekday = datetime.now().weekday()

if weekday == 0:  # monday
    yesterday = today - timedelta(days=3)
    day_before_yesterday = today - timedelta(days=4)
    yesterday_close = alpha_data["Time Series (Daily)"][str(yesterday)]["4. close"]
    day_before_close = alpha_data["Time Series (Daily)"][str(day_before_yesterday)]["4. close"]

elif weekday == 1:  # tuesday
    yesterday = today - timedelta(days=1)
    day_before_yesterday = today - timedelta(days=4)
    yesterday_close = alpha_data["Time Series (Daily)"][str(yesterday)]["4. close"]
    day_before_close = alpha_data["Time Series (Daily)"][str(day_before_yesterday)]["4. close"]

elif weekday == 2:  # wednesday
    yesterday = today - timedelta(days=1)
    day_before_yesterday = today - timedelta(days=2)
    yesterday_close = alpha_data["Time Series (Daily)"][str(yesterday)]["4. close"]
    day_before_close = alpha_data["Time Series (Daily)"][str(day_before_yesterday)]["4. close"]

elif weekday == 3:  # thursday
    yesterday = today - timedelta(days=1)
    day_before_yesterday = today - timedelta(days=2)
    yesterday_close = alpha_data["Time Series (Daily)"][str(yesterday)]["4. close"]
    day_before_close = alpha_data["Time Series (Daily)"][str(day_before_yesterday)]["4. close"]

elif weekday == 4:  # friday
    yesterday = today - timedelta(days=1)
    day_before_yesterday = today - timedelta(days=2)
    yesterday_close = alpha_data["Time Series (Daily)"][str(yesterday)]["4. close"]
    day_before_close = alpha_data["Time Series (Daily)"][str(day_before_yesterday)]["4. close"]

elif weekday == 5:  # saturday
    yesterday = today - timedelta(days=1)
    day_before_yesterday = today - timedelta(days=2)
    yesterday_close = alpha_data["Time Series (Daily)"][str(yesterday)]["4. close"]
    day_before_close = alpha_data["Time Series (Daily)"][str(day_before_yesterday)]["4. close"]

elif weekday == 6:  # sunday
    yesterday = today - timedelta(days=2)
    day_before_yesterday = today - timedelta(days=3)
    yesterday_close = alpha_data["Time Series (Daily)"][str(yesterday)]["4. close"]
    day_before_close = alpha_data["Time Series (Daily)"][str(day_before_yesterday)]["4. close"]

# calculate price percentage change
float_yes_close = float(yesterday_close)
float_before_close = float(day_before_close)
change_percentage = ((float_yes_close - float_before_close) / float_before_close) * 100

# Print the first 3 articles for "Tesla"
news_params = {
    "apiKey": NEWS_API,
    "q": COMPANY_NAME,
    "searchIn": "title",
    # "from": day_before_yesterday,
    # "to": today,
    "language": "en",
    "sortBy": "popularity",
}

news_response = requests.get(NEWS_ENDPOINT, params=news_params)
news_response.raise_for_status()
news_data = news_response.json()

counter = 0
if change_percentage >= 3 or change_percentage <= -3:  # show me related news only if stock changes by 3%
    for _ in range(1, 4):
        print(f"Title {counter + 1}: " + news_data["articles"][counter]["title"] + "\n")
        print(f"Content {counter + 1}: " + news_data["articles"][counter]["content"] + "\n")
        counter += 1

# the last step is to send a notification via email or sms which I'm not going to do that
