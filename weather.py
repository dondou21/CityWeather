import requests
import os

def get_weather(city_name):
    api_key = os.getenv('WEATHER_API_KEY')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()

        temperature = int(weather_data['main']['temp'] - 273.15)  # Convert from Kelvin to Celsius
        humidity = weather_data['main']['humidity']
        pressure = weather_data['main']['pressure']
        wind = weather_data['wind']['speed']
        condition = weather_data['weather'][0]['main']
        desc = weather_data['weather'][0]['description']

        return {
            'temperature': temperature,
            'humidity': humidity,
            'pressure': pressure,
            'wind': wind,
            'condition': condition,
            'desc': desc
        }
    except (requests.exceptions.RequestException, KeyError) as e:
        print(f"Error fetching weather data: {e}")
        return None