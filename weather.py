import requests

city = input("Enter a city: ")

# Get latitude and longitude

url = "https://geocoding-api.open-meteo.com/v1/search"

params = {
    "name": city,
    "count": 1,
    "language": "en",
    "format": "json"
}

response = requests.get(url, params=params)

print(response.status_code)
print(response.json())

latitude = response.json()["results"][0]["latitude"]
longitude = response.json()["results"][0]["longitude"]

print("Latitude:", latitude)
print("Longitude:", longitude)


# Get weather

weather_url = "https://api.open-meteo.com/v1/forecast"

weather_params = {
    "latitude": latitude,
    "longitude": longitude,
    "current": "temperature_2m,relative_humidity_2m,apparent_temperature,wind_speed_10m,weather_code"
}

weather_response = requests.get(weather_url, params=weather_params)

print(weather_response.status_code)
print(weather_response.json())


# Get weather data

weather_data = weather_response.json()

temperature = weather_data["current"]["temperature_2m"]
humidity = weather_data["current"]["relative_humidity_2m"]
feels_like = weather_data["current"]["apparent_temperature"]
wind_speed = weather_data["current"]["wind_speed_10m"]
weather_code = weather_data["current"]["weather_code"]

if weather_code == 0:
    weather_condition = "Clear sky"
elif weather_code in [1, 2, 3]:
    weather_condition = "Cloudy"
elif weather_code in [45, 48]:
    weather_condition = "Fog"
elif weather_code in [51, 53, 55, 56, 57]:
    weather_condition = "Drizzle"
elif weather_code in [61, 63, 65, 66, 67]:
    weather_condition = "Rain"
elif weather_code in [71, 73, 75, 77]:
    weather_condition = "Snow"
elif weather_code in [80, 81, 82]:
    weather_condition = "Rain showers"
elif weather_code in [85, 86]:
    weather_condition = "Snow showers"
elif weather_code in [95, 96, 99]:
    weather_condition = "Thunderstorm"
else:
    weather_condition = "Unknown"


# Display weather information

print("Weather:", weather_condition)
