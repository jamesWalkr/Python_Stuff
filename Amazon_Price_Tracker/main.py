import smtplib
import requests
from bs4 import BeautifulSoup
from email.message import EmailMessage

EMAIL = ""
GMAIL_PASSWORD = ""
TO_EMAIL = ""
URL = "https://www.amazon.com/dp/B07MXJ7QXF?ref=ppx_yo2ov_dt_b_product_details&th=1"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0",
    "Accept-Language": "en-US,en;q=0.5",
}


def send_message(email_addr, message):

    email = EmailMessage()
    email["from"] = EMAIL
    email["to"] = email_addr
    email["subject"] = "Amazon Price Alert"
    email.set_content(f"{message}")

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=GMAIL_PASSWORD)
        connection.send_message(email)


request = requests.get(url=URL, headers=HEADERS)

web_page = request.text

soup = BeautifulSoup(web_page, "lxml")

# price_span = soup.find(name="span", class_="a-price").getText()
price = float(
    soup.select_one(".reinventPricePriceToPayMargin").getText().replace("$", "")
)
title = soup.find(name="span", id="productTitle").getText().strip()

email_body = f"{title} is now {price}\n\n{URL}"
# print(email_body)

# TODO
# send email if item is with my budget

if price <= 230.00:
    send_message(TO_EMAIL, email_body)
else:
    print("This item is not in your budget")
