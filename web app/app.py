#XGBOOST prediction model
from flask import Flask, request, render_template, jsonify
import xgboost as xgb
import numpy as np
import pandas as pd 
import requests
import datetime
import os
import pytz
from dotenv import load_dotenv

app = Flask(__name__)

# Load the trained regression models
base_dir1 = os.path.dirname(os.path.abspath(__file__))  # Directory of the script
MODEL_PATH = os.path.join(base_dir1, "xgboost_Calgary.json")

base_dir2 = os.path.dirname(os.path.abspath(__file__))  # Directory of the script
MODEL_PATH2 = os.path.join(base_dir2, "xgboost_Calgary.json")


# Load environment variables from .env file
load_dotenv()
TOMORROW_API_KEY = os.getenv("TOMORROW_API_KEY")
API_NINJAS_KEY = os.getenv("API_NINJAS_KEY")

# API URLs
TOMORROW_API_URL = "https://api.tomorrow.io/v4/timelines"
CITY_API_URL = "https://api.api-ninjas.com/v1/city"

# Route: Homepage
@app.route("/")
def home():
    return render_template("index.html")

# Route: Predict energy demand based on Tomorrow.io weather data
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Extract city name from user input
        city = request.json.get("city")
        if city == "Edmonton":
                model = xgb.Booster()
                model.load_model(MODEL_PATH)
        elif city == "Calgary":
                model = xgb.Booster()
                model.load_model(MODEL_PATH2)
        else:
            return jsonify({"error": "City not provided"}), 400

        # Fetch city population and coordinates from API Ninjas
        city_response = requests.get(
            CITY_API_URL,
            headers={"X-Api-Key": API_NINJAS_KEY},
            params={"name": city}
        )
        if city_response.status_code != 200:
            return jsonify({"error": "Failed to fetch city data"}), city_response.status_code
        city_data = city_response.json()

        if not city_data:
            return jsonify({"error": "City not found"}), 404
        population = city_data[0]["population"]
        latitude = city_data[0]["latitude"]
        longitude = city_data[0]["longitude"]

        # Fetch weather data from Tomorrow.io
        params = {
            "location": f"{latitude},{longitude}",
            "fields": ["temperature", "dewPoint", "humidity"],
            "timesteps": "1h",
            "units": "metric",
            "apikey": TOMORROW_API_KEY,
        }
        weather_response = requests.get(TOMORROW_API_URL, params=params)
        if weather_response.status_code != 200:
            return jsonify({"error": "Failed to fetch weather data"}), weather_response.status_code
        weather_data = weather_response.json()

        # Prepare input data for the next 24 hours
        predictions = []
        current_time = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
        mdt_timezone = pytz.timezone("America/Denver")  # MDT timezone

        for hour in weather_data["data"]["timelines"][0]["intervals"]:
            # Extract weather features
            temp = hour["values"]["temperature"]
            dew_point_temp = hour["values"]["dewPoint"]
            relative_humidity = hour["values"]["humidity"]

            # Extract time-based features
            hour_of_day = current_time.hour
            day_of_month = current_time.day
            month_of_year = current_time.month

           # Create input DataFrame for XGBoost
            input_data = pd.DataFrame([{
                "hour": hour_of_day,
                "day": day_of_month,
                "month": month_of_year,
                "TEMP": temp,
                "DEW_POINT_TEMP": dew_point_temp,
                "RELATIVE_HUMIDITY": relative_humidity,
                "Population": population / 1_000_000  # Scale population
            }])

            # Convert to DMatrix for XGBoost
            dmatrix = xgb.DMatrix(input_data)

            # Predict energy demand
            predicted_demand = model.predict(dmatrix)[0]

            # Convert time to MDT
            mdt_time = current_time.astimezone(mdt_timezone).strftime("%Y-%m-%d %I:%M %p %Z")

            # Append the result
            predictions.append({
                "time": mdt_time,
                "temperature": float("%.2f" % (temp)),
                "predicted_demand": float("%.2f" % (predicted_demand))
            })

            # Increment time for next prediction
            current_time += datetime.timedelta(hours=1)

        return jsonify(predictions)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

# To view web interface http://127.0.0.1:5000