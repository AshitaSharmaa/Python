import requests
import os
from twilio.rest import Client

account_sid = "AC6af968ec784406c859a03694e64ed134"
auth_token = "1cfe00ee08e399c87a29bc9e4fd3a42f"
API_key = "5002bd2e10638f615892fb32f1e38b5b"
my_lat = 51.253777
my_lng = -85.323212
parameters = {
    "lat" : my_lat,
    "lon" : my_lng,
    "appid": API_key,
    "cnt" : 4,
}
URL = "https://api.openweathermap.org/data/2.5/forecast?"
response = requests.get(URL, params=parameters)
response.raise_for_status()
data = response.json()
will_rain = False
for i in range(0,4):
    if int(data["list"][i]["weather"][0]["id"]) > 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain. Please carry an umbrella ☔️with you",
        from_="+18483605705",
        to="+14374990066",
    )

