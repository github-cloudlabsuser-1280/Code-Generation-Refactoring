# Use GitHub Copilot to generate code that connects to the OpenWeatherMap API. Begin by writing a comment like # Fetch weather data from OpenWeatherMap API, which will help Copilot understand your goal and provide relevant code snippets.
# Ensure that the code includes functionality for making API requests and processing the retrieved data to display weather information like temperature, humidity, and weather conditions.

# Fetch weather data from OpenWeatherMap API
import requests

def get_weather_data(city_name):
    api_key = "52460fd4866e5fcaad00734296096341"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        weather = {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["description"]
        }
        return weather
    else:
        return None

city_name = "London"
weather_data = get_weather_data(city_name)

if weather_data:
    print(f"Temperature: {weather_data['temperature']} K")
    print(f"Humidity: {weather_data['humidity']}%")
    print(f"Weather: {weather_data['weather']}")
else:
    print("Failed to fetch weather data")

# End of script