import requests
import pickle
import pandas as pd
import numpy as np

# Load the trained model and scaler
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Function to fetch the latest data from the API
def fetch_latest_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Prepare data for prediction
def prepare_data_for_prediction(raw_data):
    # Convert raw data to a DataFrame (adjust as needed)
    df = pd.DataFrame([raw_data])
    
    # Ensure the input data matches the model's expected format
    processed_data = scaler.transform(df)
    return processed_data

# Make prediction
def predict(data):
    prediction = model.predict(data)
    return prediction

# Replace 'your_api_endpoint_here' with the actual API URL
api_url = 'https://database-trial.onrender.com/docs'
raw_data = fetch_latest_data(api_url)

if raw_data:
    processed_data = prepare_data_for_prediction(raw_data)
    prediction = predict(processed_data)
    print(f"Prediction: {prediction}")
else:
    print("No data to process.")












# import requests
# import pickle
# import numpy as np

# # Fetching the latest customer interaction
# response = requests.get("http://localhost:8000/customerInteractions/")
# latest_interaction = response.json()[-1]  # Assume last one is the latest

# # Load your pre-trained model
# with open("model.pkl", "rb") as model_file:
#     model = pickle.load(model_file)

# # Prepare data for prediction
# input_data = np.array([[latest_interaction["customer_care_calls"],
#                         latest_interaction["customer_rating"],
#                         latest_interaction["reached_on_time"],
#                         ...]])  # Add other necessary features

# # Make prediction
# prediction = model.predict(input_data)
# print(f"Prediction: {prediction}")
