from requests import *
from twilio.rest import Client
api_key = "You weather api key"
account_sid = "Your tiwilio account sid"
auth_token = "Your tiwilio auth token"
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
                         from_='replace with your own twilio trail phone number',
                         to='replace with the number to which you have to send your message'
                     )
else:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(body="You just don't need an umbrella as it going to be a brighter day 🌞",
                from_='replace with your own twilio trail phone number',
                to='replace with the number to which you have to send your message'
                )
