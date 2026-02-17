from flask import Flask, render_template, request
import os
import requests
import sys
import time

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
app = Flask(__name__, template_folder=template_dir)

@app.route("/", methods=["GET", "POST"])
def home():
  output_message = ""
  if request.method == "POST":
    location = request.form.get('location')
    action = request.form.get('action')
    def thing():
        global location
        response = (requests.get(f"https://api.weatherapi.com/v1/current.json?key=19e3ea7f765c4e42974134252252007&q={location}&aqi=yes")).json()
            if action == "is_day":
              if response["current"][jsoninput] == "1":
                  output_message = "Yes"
              elif response["current"][jsoninput] == "0":
                  output_message = "No"
            elif action == "condition":
                output_message = response["current"]["condition"]["text"]
            elif action == "co" or action == "no2" or action == "o3" or action == "so2" or action == "pm2_5" or action == "pm10" or action == "us-epa-index" or action == "gb-defra-index":
                output_message = response["current"]["air_quality"][action]
            else:
                output_message = response["current"][action]

