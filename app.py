import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open('your_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define feature names
feature_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']

def predict_house_price(features):
    # Perform prediction
    prediction = model.predict(features)
    return prediction

def main():
    st.title("House Price Prediction")

    # Create form for user input
    form = st.form(key='input_form')

    # Add input fields for each feature
    input_features = []
    for feature in feature_names:
        value = form.number_input(feature, step=0.1)
        input_features.append(value)

    # Submit button
    submitted = form.form_submit_button(label='Predict')

    # Perform prediction and display result
    if submitted:
        input_features = np.array([input_features])
        prediction = predict_house_price(input_features)
        st.success(f"The predicted house price is ${prediction[0]:.2f}")

if __name__ == '__main__':
    main()
