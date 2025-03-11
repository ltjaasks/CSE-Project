from flask import Flask, render_template, request, make_response
import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key_owm = os.getenv("OWM_API_KEY")
api_key_wa = os.getenv("WA_API_KEY")

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        if not api_key_owm:
            raise ValueError("Error: API key not found. Set OWM_API_KEY in your .env file.")
        elif not api_key_wa:
            raise ValueError("Error: API key not found. Set WA_API_KEY in your .env file.")
        return render_template('index.html')
    except Exception as error:
        response = make_response(render_template('index.html', error_message=error), 404)
        response.mimetype = 'text/html'
        return response


@app.route('/', methods=['POST'])
def showTemperatures():
    try:
        location = request.form['location'].strip(" ")
        print(location)
        owm = get_temperature_from_api(f'https://api.openweathermap.org/data/2.5/weather?q={location}&APPID={api_key_owm}&units=metric')

        wa = get_temperature_from_api(f'http://api.weatherapi.com/v1/current.json?key={api_key_wa}&q={location}&aqi=no')

        difference = round(abs(owm - wa), 2)
        avg = round((owm + wa) / 2, 2)
        return render_template('index.html', owm=owm, wa=wa, difference=difference, avg=avg, location=location.capitalize(), placeholder=location)
    except Exception as error:
        return render_template('index.html', error_message=error)
    

def get_temperature_from_api(api_url):
    response = requests.get(api_url)
    data = response.json()
    if response.status_code != 200:
        raise ValueError("Enter a valid city name")
    if "main" in data and "temp" in data["main"]:
        return data["main"]["temp"]
    elif "current" in data and "temp_c" in data["current"]:
        return data["current"]["temp_c"]
