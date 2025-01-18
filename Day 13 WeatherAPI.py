import requests

# Function to get weather data from OpenWeatherMap API
def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to display weather information
def display_weather(data):
    if data:
        city = data['name']
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        print(f"City: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Weather: {weather_description}")
    else:
        print("Error fetching weather data.")

# Main script
api_key = 'your_api_key_here'  # Replace with your OpenWeatherMap API key
city = input("Enter the city name: ")
weather_data = get_weather(city, api_key)
display_weather(weather_data)