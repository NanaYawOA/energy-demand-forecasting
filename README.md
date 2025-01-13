# 🌍 Energy Demand Forecast App

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)  
![Flask](https://img.shields.io/badge/Flask-2.0+-success)  
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-TensorFlow%2C%20XGBoost-orange)  
![API Integration](https://img.shields.io/badge/API%20Integration-Tomorrow.io%2C%20ApiNinjas-brightgreen)

## 🔥 Overview

The **Energy Demand Forecast App** is a cutting-edge machine learning web application that predicts real-time energy demand and forecasts electricity usage based on weather data. This app is designed to help governments, businesses, and individuals plan for energy consumption, reduce energy waste, and optimize costs in a sustainable way. This first version focuses on predicting electricity demand for Calgary and Edmonton, Alberta, Canada.

---

## 🚀 Features

- **Real-Time Energy Demand Prediction**:
  - Uses a trained XGBoost regression model for accurate energy demand forecasts.
- **Weather Data Integration**:
  - Fetches weather data from the [Tomorrow.io API](https://www.tomorrow.io/) to enhance prediction accuracy.
- **Population-Based Insights**:
  - Incorporates population data from the [API Ninjas City API](https://api-ninjas.com/api/city) for more precise predictions.
- **Interactive Dashboard**:
  - A user-friendly dashboard built with Flask, HTML and CSS to visualize predictions.
- **City-Specific Insights**:
  - Select cities (e.g., Calgary, Edmonton) and visualize specific forecasts.

---

## 🛠️ Technologies

This app is built with the following technologies:

- **Backend**: Flask
- **Frontend**: HTML, CSS,
- **Machine Learning**: TensorFlow, XGBoost
- **Data Visualization**: Matplotlib
- **APIs**:
  - Tomorrow.io Weather API
  - API Ninjas City API

---

## 📂 Repository Structure
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── templates/
│   ├── dashboard.html        # Dashboard for visualization
├── static/
│   ├── styles.css            # Custom CSS for styling
├── models/
│   ├── xgboost_model.pkl     # Trained XGBoost model
├── data/
│   ├── historical_data.csv   # Sample training dataset
├── .env                      # Environment variables (not included in GitHub)

---

## 🚀 Getting Started

### Prerequisites

1. Python 3.8 or later
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
API keys:
Create a .env file in the root directory:
env
Copy code
TOMORROW_API_KEY=your_tomorrow_api_key
API_NINJAS_KEY=your_api_ninjas_key
Running the App
Start the Flask server:
bash
Copy code
python app.py
Access the app: Open your browser and navigate to http://127.0.0.1:5000.

---

🧑‍💻 Development Workflow
Training the Model
Use the dataset data/historical_data.csv for training.
Preprocess and split the data.
Train the XGBoost model:
python
Copy code
from xgboost import XGBRegressor
model = XGBRegressor()
model.fit(X_train, y_train)
Save the model:
python
Copy code
import joblib
joblib.dump(model, "models/xgboost_model.pkl")

---

⚙️ Features Demo
📊 Interactive Dashboard
The app provides an intuitive interface to:

Select cities
View real-time energy demand
Visualize key weather parameters affecting energy usage, such as temperature and humidity
🌦️ Weather Integration
The app fetches live weather data, including:

Temperature
Relative humidity
Dew point temperature
⚡ Machine Learning Predictions
Predictions are generated using a pre-trained XGBoost model for maximum accuracy.

🌟 Future Enhancements
Expand support to more cities.
Include renewable energy production predictions.
Integrate with IoT devices for direct energy monitoring.
Add multi-lingual support for the dashboard.


---


📄 License
This project is licensed under the MIT License.

💡 Acknowledgments
Tomorrow.io API
API Ninjas
XGBoost
