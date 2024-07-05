from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

# Load your trained model and features
model_filename = 'gradient_boosting_model.sav'
features_filename = 'model_features.pkl'

with open(model_filename, 'rb') as file:
    model = pickle.load(file)

with open(features_filename, 'rb') as file:
    model_features = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html', features=model_features)

@app.route('/predict', methods=['POST'])
def predict():
    # Collect input values from the form
    input_values = [float(request.form[attr]) for attr in model_features]

    # Create DataFrame from input for prediction
    input_df = pd.DataFrame([input_values], columns=model_features)
    
    # Handle missing values by filling with the mean of each column (same as training)
    input_df.fillna(input_df.mean(), inplace=True)

    # Predict insurance cost
    predicted_cost = model.predict(input_df)[0]

    return render_template('index.html', prediction_text=f'Predicted Insurance Cost: ₹{predicted_cost:.2f}', features=model_features)

if __name__ == '__main__':
    app.run(debug=True)
