import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow import keras
import matplotlib.pyplot as plt

model_path="models/tensorflow/Edmonton_LSTM_model.keras"   # Path to save the trained model
data_path="Data/Clean Data/Edmonton_processed_data.csv"    # Path to the preprocessed data

# Load the data
data = pd.read_csv(data_path)

# Scale the data
scaler = MinMaxScaler()
data['Electricity Demand'] = scaler.fit_transform(data[['Electricity Demand']])
#data['RELATIVE_HUMIDITY'] = scaler.fit_transform(data[['RELATIVE_HUMIDITY']])
data['Population'] = scaler.fit_transform(data[['Population']])
#data['DEW_POINT_TEMP'] = scaler.fit_transform(data[['DEW_POINT_TEMP']])

# Function to save the trained model
def save_model(model, model_path):
    model.save(model_path)
    print(f"Model saved to {model_path}")

# Create time-based features
def create_sequences(data, sequence_length):
    X, y = [], []
    for i in range(len(data) - sequence_length):
        X.append(data[i:i + sequence_length, :-1])  # Past `sequence_length` features
        y.append(data[i + sequence_length, -1])    # Target value
    return np.array(X), np.array(y)

sequence_length = 24  # Use past 24 hours to predict the next value
dataset = data[['hour', 'day','month','TEMP', 'Electricity Demand','DEW_POINT_TEMP','RELATIVE_HUMIDITY','Population']].values

X, y = create_sequences(dataset, sequence_length)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build the LSTM model
model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(X_train.shape[1], X_train.shape[2])),
    LSTM(50),
    Dense(1)  # Output layer for predicting a single value
])

# Compile the model
model.compile(optimizer=Adam(learning_rate=0.001), loss="mean_squared_error")

# Train the model
history = model.fit(X_train, y_train, epochs=20, batch_size=32, validation_data=(X_test, y_test), verbose=1)

# Save the trained model
save_model(model, model_path)

# Evaluate the model
test_loss = model.evaluate(X_test, y_test)
print(f"Test Loss: {test_loss}")

# Predict
predictions = model.predict(X_test)
predictions_rescaled = scaler.inverse_transform(predictions.reshape(-1, 1))
y_test_rescaled = scaler.inverse_transform(y_test.reshape(-1, 1))

# Visualization: Actual vs Predicted
plt.figure(figsize=(10, 6))
plt.plot(y_test_rescaled[:100], label="Actual", color="blue")
plt.plot(predictions_rescaled[:100], label="Predicted", color="orange", linestyle="--")
plt.title("Energy Demand: Actual vs Predicted (LSTM)")
plt.xlabel("Sample Index")
plt.ylabel("Energy Demand")
plt.legend()
plt.grid()
plt.show()

