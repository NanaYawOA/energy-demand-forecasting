import pandas as pd

def preprocess_data(file_path):
    # Load dataset
    data = pd.read_csv(file_path, parse_dates=['Date (MPT)'])
    
    # Handle missing values
    data.fillna(method='ffill', inplace=True)
    
    # Create time-based features
    data['hour'] = data['Date (MPT)'].dt.hour
    data['day_of_week'] = data['Date (MPT)'].dt.dayofweek
    
    return data

if __name__ == "__main__":
    processed_data = preprocess_data("C:/Users/Hp/Desktop/ML AND AI PROJECTS/energy-demand-forecasting/data/Clean Data/Electricity Demand_Climate_Population and Housing_Edmonton_Hourly_Clean.csv")
    processed_data.to_csv("C:/Users/Hp/Desktop/ML AND AI PROJECTS/energy-demand-forecasting/data/Clean Data/Edmonton_processed_data.csv", index=False)
    processed_data = preprocess_data("C:/Users/Hp/Desktop/ML AND AI PROJECTS/energy-demand-forecasting/data/Clean Data/Electricity Demand_Climate_Population and Housing_Calgary_Hourly_Clean.csv")
    processed_data.to_csv("C:/Users/Hp/Desktop/ML AND AI PROJECTS/energy-demand-forecasting/data/Clean Data/Calgary_processed_data.csv", index=False)