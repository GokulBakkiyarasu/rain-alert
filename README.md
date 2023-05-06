# Umbrella Advisory And Rain Alert

This program uses the WeatherAPI to get weather forecast data and the Twilio API to send an SMS message to the user indicating whether they should bring an umbrella or not. 

![1683399797357](https://user-images.githubusercontent.com/87391223/236642855-129a7c0e-4755-42f7-945b-5e23c06d943d.jpg)


## Features
- Uses WeatherAPI to retrieve weather forecast data
- Uses Twilio API to send SMS messages
- Sends an SMS message advising the user whether they should bring an umbrella or not

## Getting Started
To get started with this program, you need to have a WeatherAPI and Twilio account. You can sign up for a free account at [WeatherAPI](https://www.weatherapi.com/) and [Twilio](https://www.twilio.com/). You will also need to install the requests and twilio python packages. 

### Prerequisites
- Python 3.x
- requests
- twilio

### Installation
1. Clone the repository: 
   ```
   git clone https://github.com/your_username/rain-alert.git
   ```
2. Install dependencies:
   ```
   pip install requests
   pip install twilio
   ```
3. Set environment variables:
   ```
   export WEATHER_API_KEY="your_weather_api_key"
   export TWILIO_ACCOUNT_SID="your_twilio_account_sid"
   export TWILIO_AUTH_TOKEN="your_twilio_auth_token"
   ```
4. Run the program:
   ```
   main.py
   ```

## Usage
1. Retrieve weather data: The program retrieves weather forecast data using the WeatherAPI. 
2. Check if it will rain: The program checks if it will rain in the next 12 hours by analyzing the weather condition codes in the weather data.
3. Send SMS message: The program sends an SMS message to the user advising them whether they should bring an umbrella or not based on the result of the previous step.

## File structure
```
├── main.py      # Main program file
```

## Functions:
Retrieving Weather Data:
```python
from requests import *

api_key = "Enter the api_key of your own weather api account"

parameters = {
    "q": [11.601730, 79.518740],
    "key": api_key,
}
response = get(url="http://api.weatherapi.com/v1/forecast.json",  params=parameters)
response.raise_for_status()
weather_data = response.json()
```
Checking if it will rain:
```python
hourly_weather_data = weather_data["forecast"]["forecastday"][0]["hour"]
twelve_hours_report = hourly_weather_data[8:20]
weather_codes = []
for i in range(len(twelve_hours_report)):
    weather_codes.append(twelve_hours_report[i]["condition"]["code"])
will_rain = False
for codes in weather_codes:
    if codes == 1063 or 1180 <= codes <= 1200:
        will_rain = True
```
Sending SMS Message:
```python
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
```
## Contributing
Contributions to this project are welcome. To contribute, follow these steps:
1. Fork this repository
2. Create a new branch (`git checkout -b feature/new-feature`)
3. Make and commit your changes (`git commit -am "Add new feature"`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a new Pull Request
## Find me on
[![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-Profile-informational?style=flat&logo=linkedin&logoColor=white&color=0D76A8)](https://www.linkedin.com/in/gokul-bakkiyarasu-531535251)
