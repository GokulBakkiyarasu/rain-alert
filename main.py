from requests import *
from twilio.rest import Client
api_key = "8115df57eef541fbbad71228230405"
account_sid = "AC2ab0b55d07f4959a9eefb943bbefc55d"
auth_token = "e3a9e6ca78d53f250f7fddea13e19018"
parameters = {
    "q": [11.601730, 79.518740],
    "key": api_key,
}
response = get(url="http://api.weatherapi.com/v1/forecast.json",  params=parameters)
response.raise_for_status()
weather_data = response.json()
hourly_weather_data = weather_data["forecast"]["forecastday"][0]["hour"]
twelve_hours_report = hourly_weather_data[8:20]
weather_codes = []
for i in range(len(twelve_hours_report)):
    weather_codes.append(twelve_hours_report[i]["condition"]["code"])
will_rain = False
for codes in weather_codes:
    if codes == 1063 or 1180 <= codes <= 1200:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                         body="Bringing an umbrella is advisory as it will rain today ☔",
                         from_='+13184884454',
                         to='+919047989145'
                     )
else:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(body="You just don't need an umbrella as it going to be a brighter day 🌞",
                from_='+13184884454',
                to='+919047989145'
                )