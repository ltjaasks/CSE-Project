from flask import Flask
from flask import render_template, request
import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key_owm = os.getenv("OWM_API_KEY")
if not api_key_owm:
    raise ValueError("API key not found. Set OWM_API_KEY in your .env file.")
api_key_wa = os.getenv("WA_API_KEY")
if not api_key_wa:
    raise ValueError("API key not found. Set WA_API_KEY in your .env file.")

app = Flask(__name__, template_folder="../templates")


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def showTemperatures():
    location = request.form['location']
    response_owm = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={location}&APPID={api_key_owm}&units=metric')
    data_owm = response_owm.json()

    response_wa = requests.get(f'http://api.weatherapi.com/v1/current.json?key={api_key_wa}&q={location}&aqi=no')
    data_wa = response_wa.json()

    owm = data_owm["main"]["temp"]
    wa = data_wa["current"]["temp_c"]
    difference = round(abs(owm - wa), 2)
    avg = round((owm + wa) / 2, 2)
    return render_template('index.html', owm=owm, wa=wa, difference=difference, avg=avg)
