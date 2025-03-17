<h1>CSE Course Project</h1>

This is a course project for the course TJTS5901 Continuous Software Engineering. The implemented project is a simple web application made with Python's Flask library. The application fetches current Weather data from two Weather APIs with given city and then compares them (difference and average). 

The project can be run locally:
1. Open Terminal (Command line, Bash etc. depending which system you are using)
2. Make sure you have Git installed on your device (test by writing git --version in the terminal) and clone the project to your device with **git clone https://github.com/ltjaasks/CSE-Project.git**. Move to the project folder with **cd** command.
3. Make sure you have Python 3.10+ installed on your device (you can test it by writing **python --version** in the terminal)
4. Initialize virtual environment (unless you want to install every package in your device) by writing **virtualenv venv**
5. Activate virtual environment by writing **.\venv\Scripts\activate** (Windows) or **source /venv/bin/activate** (Linux)
6. Install the needed requirements with requirements.txt file by typing **pip install -r requirements.txt**
7. Get your OpenWeatherMap and WeatherAPI API keys from their website.
8. Create .env file in the project folder and add there the following lines: <br>
    OWM_API_KEY=your personal API key <br>
    WA_API_KEY=your personal API key
9. Run the application from terminal by writing **flask --app app.py run**
10. Open browser and locate to the address shown in the terminal (typically 127.0.0.1:5000/)
11. Use the application

Instructions for running tests and Bandit:
TODO
