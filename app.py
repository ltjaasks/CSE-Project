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
        response_owm = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={location}&APPID={api_key_owm}&units=metric')
        data_owm = response_owm.json()
        print(data_owm)
        response_wa = requests.get(f'http://api.weatherapi.com/v1/current.json?key={api_key_wa}&q={location}&aqi=no')
        data_wa = response_wa.json()

        if response_owm.status_code == 401 or response_wa.status_code == 401:
            raise ValueError("Invalid API key")
        elif response_owm.status_code != 200 or response_wa.status_code != 200:
            raise ValueError("Enter a valid city name")
        
        location_wa = f"{data_wa["location"]["name"]}, {data_wa["location"]["country"]}"
        location_owm = f"{data_owm["name"]}, {data_owm["sys"]["country"]}"

        owm = data_owm["main"]["temp"]
        wa = data_wa["current"]["temp_c"]
        difference = round(abs(owm - wa), 2)
        avg = round((owm + wa) / 2, 2)
        return render_template('index.html', owm=owm, wa=wa, difference=difference, avg=avg, location_wa=location_wa, location_owm=location_owm, placeholder=location)
    except Exception as error:
        return render_template('index.html', error_message=error, placeholder=location)
