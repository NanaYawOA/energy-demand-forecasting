import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

# Load preprocessed data
data = pd.read_csv("Data/Clean Data/Calgary_processed_data.csv")


# Define features and target
X = data[['hour', 'day', 'month', 'TEMP','DEW_POINT_TEMP','RELATIVE_HUMIDITY','Population']]
y = data['Electricity Demand']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train XGBoost model
model = XGBRegressor(n_estimators=200, learning_rate=0.1, max_depth=5)
model.fit(X_train, y_train)

#save model
model.save_model('models/xgbost/xgboost_Calgary.json')

# Evaluate model
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
print(f"Mean Absolute Error: {mae}")

# Visualization: Predicted vs Actual
def plot_predictions(y_test, predictions):
    plt.figure(figsize=(10, 6))
    plt.plot(y_test.values[:100], label="Actual", marker="o", linestyle="-", color="blue")
    plt.plot(predictions[:100], label="Predicted", marker="x", linestyle="--", color="orange")
    plt.title("Energy Demand: Actual vs Predicted")
    plt.xlabel("Sample Index")
    plt.ylabel("Energy Demand")
    plt.legend()
    plt.grid()
    plt.show()

# Call visualization function
plot_predictions(y_test, predictions)
