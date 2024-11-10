import requests
import pickle
import numpy as np

# Fetching the latest customer interaction
response = requests.get("http://localhost:8000/customerInteractions/")
latest_interaction = response.json()[-1]  # Assume last one is the latest

# Load your pre-trained model
with open("model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Prepare data for prediction
input_data = np.array([[latest_interaction["customer_care_calls"],
                        latest_interaction["customer_rating"],
                        latest_interaction["reached_on_time"],
                        ...]])  # Add other necessary features

# Make prediction
prediction = model.predict(input_data)
print(f"Prediction: {prediction}")
