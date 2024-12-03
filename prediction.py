import numpy as np
import pickle

# Load the trained model and scaler
with open('neural_network_model.pkl', 'rb') as file:
    model, scaler = pickle.load(file)

# Define a function to make predictions
def predict_output(input_values):
    # Scale the input values
    scaled_input = scaler.transform([input_values])
    # Make prediction
    prediction = model.predict(scaled_input)
    return prediction

# Example input values
input_values = [1.0, 2.0, 3.0, 4.0]  # Change this to your actual input values

# Make prediction
output_values = predict_output(input_values)

print("Predicted output values:", output_values)
