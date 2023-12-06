import requests
import smtplib
from bs4 import BeautifulSoup
import lxml

amazon_product_url = "https://www.amazon.com/Certified-Refurbished-Amazon-eero-system/dp/B0BHKR3Z9Y?ref_=Oct_DLandingS_D_7b0b3096_1"
hotmail_user = "mj.habib4@hotmail.com"
hot_pass = "pass"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,fa-IR;q=0.8,fa;q=0.7",
}

response = requests.get(url=amazon_product_url, headers=headers)

soup = BeautifulSoup(response.text, "lxml")
price = soup.find("span", class_="a-offscreen").getText().strip("$")

if float(price) < 100:
    print(f"Subject: New deal\n\n The price of this product: \n{amazon_product_url}\n dropped to: '${price}'. Enjoy")
    # with smtplib.SMTP("smtp.office365.com", port=587) as connection:
    #     connection.starttls()
    #     connection.login(user=hotmail_user, password=hot_pass)
    #     connection.sendmail(from_addr=hotmail_user, to_addrs=hotmail_user,
    #                         msg=f"Subject: New deal\n\n The price of this product: \n{amazon_product_url}\n dropped to: '${price}'. Enjoy")
else:
    print("Maybe some other time")
