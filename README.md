<h1>CSE Course Project</h1>

This is a course project for the course TJTS5901 Continuous Software Engineering. The implemented project is a simple web application made with Python's Flask library. The application fetches current Weather data from two weather APIs with given city and then compares them (difference and average). The application is running on https://z0nsk1.pythonanywhere.com/ <br><br>
Tech Stack:
- Bandit (Security of the code)
- Docker (Containerization of the application)
- Flask (WSGI web application framework for Python)
- Github Actions (CI/CD pipeline)
- Git & Github (Version control)
- Kubernetes (Deployment of the application)
- Minikube (Local Kubernetes)
- Python 3.11+ (Programming language)
- Pytest (Test runner & testing framework for Python)
- Pytest-BDD (BDD framework for Pytest)


The project can be run locally:
1. Open Terminal (Command line, Bash etc. depending which system you are using)
2. Make sure you have Git installed on your device (test by writing git --version in the terminal) and clone the project to your device with <pre><code>git clone https://github.com/ltjaasks/CSE-Project.git</code></pre> Move to the project folder with cd command <pre><code>cd project-folder</code></pre>
3. Make sure you have Python 3.11+ installed on your device (you can test it by writing **python --version** in the terminal)
5. Initialize virtual environment (unless you want to install every package in your device) by writing <pre><code>virtualenv venv</code></pre>
7. Activate virtual environment in Windows by writing <pre><code>.\venv\Scripts\activate</code></pre> or in Linux <pre><code>source /venv/bin/activate</code></pre>
8. Install the needed requirements with requirements.txt file by typing <pre><code>pip install -r requirements.txt</code></pre>
9. Get your OpenWeatherMap and WeatherAPI API keys from their website.
10. Create .env file in the project folder and add there the following lines: <pre><code>OWM_API_KEY=your personal API key
WA_API_KEY=your personal API key</code></pre>
12. Run the application from terminal by writing <pre><code>flask run</code></pre>
13. Open browser and locate to the address shown in the terminal (typically 127.0.0.1:5000/)
