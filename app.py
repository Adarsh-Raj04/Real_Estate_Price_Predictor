import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open('your_model.pkl', 'rb') as f:
    model = pickle.load(f)


# Define the feature names
feature_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']

# Create the input form
st.title('Real Estate Price Predictor')

# Input form for feature values
feature_inputs = []
for feature in feature_names:
    value = st.number_input(f"Enter value for {feature}", key=feature)
    feature_inputs.append(value)

# Predict function
def predict_price(features):
    input_df = pd.DataFrame([features], columns=feature_names)
    prediction = model.predict(input_df)[0]
    return prediction

# Predict button
if st.button('Predict'):
    price = predict_price(feature_inputs)
    st.success(f'The predicted price is ${price:.2f}')
