from flask import Flask, render_template, request, make_response
import requests
from dotenv import load_dotenv
import os
import math

load_dotenv() # Load dotenv file
app = Flask(__name__) # Initialize Flask app


def get_api_keys():
    api_key_owm = os.getenv("OWM_API_KEY") # Get OWM API key from .env file
    api_key_wa = os.getenv("WA_API_KEY") # Get WA API key from .env file
    return api_key_owm, api_key_wa # Return API keys


# Initalize the front page
@app.route('/')
def hello():
    try:
        api_key_owm, api_key_wa = get_api_keys() # Get API keys from function
        # Handling cases where API keys are not found
        if not api_key_owm or api_key_owm == None:
            raise NameError("Error: API key not found. Set OWM_API_KEY in your .env file.")
        elif not api_key_wa or api_key_wa == None:
            raise NameError("Error: API key not found. Set WA_API_KEY in your .env file.")
        response = make_response(render_template('index.html'), 200) # Make response object
        response.mimetype = 'text/html' # Set mimetype for the response
        return response
    except Exception as error:
        print("Error: ", error)
        # Error handling, here we return the error message and HTTP code
        response = make_response(render_template('index.html', error_message=error), 404)
        response.mimetype = 'text/html'
        return response


@app.route('/', methods=['POST'])
def showTemperatures():
    try:
        api_key_owm, api_key_wa = get_api_keys()
        location = request.form['location'].strip(" ")
        print(location)
        owm = get_temperature_from_api(f'https://api.openweathermap.org/data/2.5/weather?q={location}&APPID={api_key_owm}&units=metric', location)
        wa = get_temperature_from_api(f'http://api.weatherapi.com/v1/current.json?key={api_key_wa}&q={location}&aqi=no', location)
        
        owm_temp = owm["main"]["temp"] # Set OWM API temperature
        wa_temp = wa["current"]["temp_c"] # Set WA API temperature
        owm_location = f"{owm['name']}, {owm['sys']['country']}" # Set OWM API location (city, country)
        wa_location = f"{wa['location']['name']}, {wa['location']['country']}" # Set WA API location (city, country)

        # If APIs return data (probably) from different cities, show a note for the user
        if not math.isclose(owm_temp, wa_temp, abs_tol=0.5):
            print("Different cities")
            note = "Note, the APIs probably requested the weather data from different cities"
        else:
            note = ""

        difference = round(abs(owm_temp - wa_temp), 2) # Calculate the difference between the two temperatures
        avg = round((owm_temp + wa_temp) / 2, 2) # Calculate the average temperature
        # Make response object with the data
        response = make_response(render_template('index.html', owm=owm_temp, wa=wa_temp, owm_location=owm_location, wa_location=wa_location, difference=difference, avg=avg, placeholder=location, note=note), 200)
        response.mimetype = 'text/html' # Set mimetype for the response
        return response
    except Exception as error:
        # Error handling: if an error raises, return the error message and HTTP code
        response = make_response(render_template('index.html', error_message=error, placeholder=location), 404)
        response.mimetype = 'text/html'
        return response
    

# Function to get temperature from API
# Arguments: API URL, location
# Returns: JSON data from API or error
def get_temperature_from_api(api_url, location = None):
    try: 
        response = requests.get(api_url, timeout=5) # Make a GET request to the API
        data = response.json() # Convert response to JSON
        # Error handlings
        if response.status_code == 401 or response.status_code == 401: # If API key is invalid
            raise ValueError("Invalid API key")
        elif response.status_code != 200:
            raise ValueError("Enter a valid city name") # If city name is invalid
        return data
    except Exception as error:
        raise error