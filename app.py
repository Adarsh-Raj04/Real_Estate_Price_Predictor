import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('model.joblib')

# Function to preprocess user input
def preprocess_input(user_input):
    # Create a DataFrame with the user input
    input_data = pd.DataFrame(user_input, index=[0])

    # Perform any necessary preprocessing on the input data
    # ...

    return input_data

# Function to predict the real estate price
def predict_price(input_data):
    # Make predictions using the loaded model
    predictions = model.predict(input_data)

    # Return the predicted price
    return predictions[0]

# Main app code
def main():
    # Set the app title
    st.title("Real Estate Price Predictor")

    # Create input fields for user input
    crim = st.number_input("CRIM")
    zn = st.number_input("ZN")
    indus = st.number_input("INDUS")
    chas = st.number_input("CHAS")
    nox = st.number_input("NOX")
    rm = st.number_input("RM")
    age = st.number_input("AGE")
    dis = st.number_input("DIS")
    rad = st.number_input("RAD")
    tax = st.number_input("TAX")
    ptratio = st.number_input("PTRATIO")
    b = st.number_input("B")
    lstat = st.number_input("LSTAT")

    # Create a dictionary with the user input
    user_input = {
        'CRIM': crim,
        'ZN': zn,
        'INDUS': indus,
        'CHAS': chas,
        'NOX': nox,
        'RM': rm,
        'AGE': age,
        'DIS': dis,
        'RAD': rad,
        'TAX': tax,
        'PTRATIO': ptratio,
        'B': b,
        'LSTAT': lstat
    }

    # Preprocess the user input
    input_data = preprocess_input(user_input)

    # Check if the user has provided all the required input fields
    if st.button("Predict"):
        # Make predictions and display the result
        price = predict_price(input_data)
        st.success(f"The predicted price is: ${price:.2f}")

# Run the app
if __name__ == '__main__':
    main()
