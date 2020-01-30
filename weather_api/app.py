from flask import Flask, render_template, request
from dotenv import load_dotenv
import requests
import os

TENOR_API_KEY = os.getenv("TENOR_API_KEY")

app = Flask(__name__)
load_dotenv()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/weather")
def weather():
    return render_template("weather_form.html")


@app.route("/weather_results")
def weather_results_page():
    users_city = request.args.get("city")
    params = {
        "q": users_city,
        "appid": TENOR_API_KEY
    }
    response = requests.get(
        'http://api.openweathermap.org/data/2.5/weather', params=params)

    response_json = response.json()
    temperature = response_json["main"]["temp"]
    temperature_convert = (temperature * 9/5) - 459.67

    return render_template("weather_results.html",
                           temperature=temperature_convert, city=users_city)
