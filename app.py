from flask import Flask, render_template, request
import requests
import json
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == "POST":
        city = request.form['city']
        country = request.form['country']
        api_key = "07fc5a09693832c0626af899c3036dd9"

        weather_url = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},{country}&units=metric')

        weather_data = weather_url.json()

        temp = round(weather_data['main']['temp'])
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']

        return render_template("result.html", temp=temp, humidity=humidity, wind_speed=wind_speed, city=city)

    return render_template("index.html")

app.run('0.0.0.0', port=80)
