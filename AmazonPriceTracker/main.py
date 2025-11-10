import requests
from bs4 import BeautifulSoup
import smtplib
MY_EMAIL ="sharmaas.sharma@gmail.com"
MY_PASSWORD = "vunhuqjzkczawvcs"

URL = "https://appbrewery.github.io/instant_pot/"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
title = soup.find(id = "productTitle").get_text().strip()
price_tag = soup.select_one(".aok-offscreen")
price = float(price_tag.get_text().split("$")[1])
print(price)
Target_Price = 100
if price < Target_Price:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user = MY_EMAIL, password = MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs= "ashitasharma@myyahoo.com",msg= f"Subject: Price drop!!  \n\n {title} \n Current Price: ${price} Go to this link to buy the product now: {URL}".encode("utf-8"))
