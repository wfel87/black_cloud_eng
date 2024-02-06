# app.py
from flask import Flask, render_template, request
import requests

app = Flask(__name__, template_folder='/Users/Wes/Desktop/python projects/HTML/templates', static_folder='/Users/Wes/Desktop/python projects/HTML/templates/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    api_key = '12f1d0b92c45b59c91ef8b5096b23e0e'  # Replace with your OpenWeatherMap API key
    city = request.form['city']
    result = fetch_weather(api_key, city)
    return render_template('index.html', result=result)

def fetch_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'imperial'
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        city_name = data['name']
        return f"Current weather in {city_name}: Temperature: {temperature}°F, Description: {description.capitalize()}"
    else:
        return f"Failed to fetch weather information. Status Code: {response.status_code}"
if __name__ == "__main__":
    app.run()