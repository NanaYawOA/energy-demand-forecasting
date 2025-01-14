# 🌍 Energy Demand Forecast App

![Python](https://img.shields.io/badge/Python-3.12%2B-blue)  
![Flask](https://img.shields.io/badge/Flask-2.0+-success)  
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-TensorFlow%2C%20XGBoost-orange)  
![API Integration](https://img.shields.io/badge/API%20Integration-Tomorrow.io%2C%20ApiNinjas-brightgreen)

## 🔥 Overview

The **Energy Demand Forecast App** is a web application that uses the XGBoost regressor machine learning model to predict real-time energy demand and forecasts electricity usage based on weather data. This app is designed to help governments, businesses, and utility companies plan for energy production and consumption, reduce energy waste, and optimize costs in a sustainable way. This first version focuses on predicting electricity demand for Calgary and Edmonton, Alberta, Canada.

---

## 🚀 Features
- **📊 Interactive Dashboard**:
  
  The app provides a user-friendly dashboard built with Flask, HTML and CSS to visualize predictions. In the dashboard you can:
  - Select cities
  - View real-time energy demand
  - Visualize key weather parameters affecting energy usage, such as temperature  
- **⚡ Real-Time Energy Demand Prediction**:
  - Uses a trained XGBoost regression model for accurate energy demand forecasts.  
- **🌦️Weather Data Integration**:
  - Fetches weather data from the [Tomorrow.io API](https://www.tomorrow.io/) to enhance prediction accuracy. 
- **Population-Based Insights**:
  - Incorporates population data from the [API Ninjas City API](https://api-ninjas.com/api/city) for more precise predictions.  
- **City-Specific Insights**:
  - Select cities (e.g., Calgary, Edmonton) and visualize specific forecasts. 
- **🌟 Future Enhancements**:
  - Expand support to more cities.
  - Include renewable energy production predictions.
  - Integrate with IoT devices for direct energy monitoring.
  - Add multi-lingual support for the dashboard.

---

## 🛠️ Technologies

This app is built with the following technologies:

- **Backend**: Flask
- **Frontend**: HTML, CSS,
- **Machine Learning**: TensorFlow, XGBoost, Linear Regression
- **Data Visualization**: Matplotlib
- **APIs**:
  - Tomorrow.io Weather API
  - API Ninjas City API

---

## 📂 Repository Structure

├── ML training + Data        # ML training scripts, models and data

│   ├── Data                  # Raw and processed data files

│   ├── Models                # trained ML models

├── webapp                    # Files for local web app deployment

│   ├── app.py                # Python app for energy prediction

│   ├── dashboard.html        # HTML, CSS data for UI

├── README.md                 # Project documentation

---

## 🚀 Getting Started

### Prerequisites:
1. Python 3.12 or later
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

### API keys:
Create a .env file in the root directory:

TOMORROW_API_KEY=your_tomorrow_api_key

API_NINJAS_KEY=your_api_ninjas_key

### Running the App locally;
Start the Flask server: by running python app.py from the webapp directory
Access the app: Open your browser and navigate to http://127.0.0.1:5000.

---

## 🧑‍💻 Machine Learning Development Workflow
### Data sources and processing:
- [Historical hourly climate data, 2015-2024](https://climate-change.canada.ca/climate-data/#/hourly-climate-data)
- [Historical population data,2015- 2024](https://regionaldashboard.alberta.ca/region/calgary/population/#/?from=2014&to=2023)
- [Historical electricity demand, 2015-2024](https://public.tableau.com/app/profile/market.analytics/viz/AnnualStatistics_16161854228350/Introduction)
- Relevant data was extracted and processed to obtain two datasets for the cities of Calgary and Edmonton respectively, providing Climate, Population and Electricity demand information.
- The cleaned supervised dataset has the follow properties:
  - 17 features of which 7 were used in training ML models
  - 86928 rows of data for each city   
### ML Model selection and training:
3 supervised learning ML Models were trained with a training data to test data split of 80% and 20%. Model performance was assessed with the following results:

![image](https://github.com/user-attachments/assets/321953fe-174d-4705-8d93-b5e4aab6a72f)
- From the above table it is clear that the XGBoost regressor is the best training model since for both datasets it has the lowest RMSE(Root Mean Squared Error) and the highest R Square of 0.88. This R Squared value implies that 88% of the variance in the dependent variable is explained by the model hence the model does a good job of understanding the relationship between the independent and dependent variables.
- XGBoost regressor model ranks second best in terms of the time required to train the model, but outclasses all the other models in terms of accuracy.
- By this analysis the best ML model for deployment of the energy demand forecasting webapp is the XGboost regressor.
![image](https://github.com/user-attachments/assets/a69553a2-c95c-4b34-845f-5a269cfbc2da)

---

## 📄 License
This project is licensed under the MIT License.

## 💡 Acknowledgments
- Tomorrow.io API
- API Ninjas
- XGBoost
