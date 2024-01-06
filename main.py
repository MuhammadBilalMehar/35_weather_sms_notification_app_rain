import requests
import os
from twilio.rest import Client

# OWM_endpoint = "https://pro.openweathermap.org/data/2.5/forecast/hourly"
# OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"

OWM_endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "493289eee074ff0c3bc9e813a7457b7f"
# api_key = os.environ.get("OWM_API_KEY")

account_sid = "ACbaeeb29afee61d40c4812b59f5bf560a"
auth_token = "d3d6fabf167a464bf5f627000438a47a"
# auth_token = os.environ.get("AuthT")

wheather_prams = {
    "lat":30.829100,
    "lon":72.144240,
    "appid":api_key,
    # "exclude":"current,minutely,daily"
}
response = requests.get(OWM_endpoint,params=wheather_prams)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["weather"][0]["id"]
# weather_slice = weather_data["hourly"][:12]

will_rain = False

if int(weather_slice) > 700:
    will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Sania I Love u please Leave an umbrela ☂️",
        from_="+13036474357",
        to='+923164499323'
    )
    print(message.status)
    