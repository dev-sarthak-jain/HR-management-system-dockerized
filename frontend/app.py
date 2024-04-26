import streamlit as st
import pandas as pd
import requests
import json

# Function to send JSON to API and get predictions
def send_json(data, url="http://127.0.0.1:8000/api/attrition_prediction/"):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data, headers=headers)
    print(response)
    return response.json()

def app():
    st.title('Employee Attrition Prediction App')
    
    # File uploader widget
    uploaded_file = st.file_uploader("Choose a CSV file", type=['csv'])
    if uploaded_file is not None:
        # Reading the uploaded CSV file
        df = pd.read_csv(uploaded_file)
        
        # Converting each row to JSON and sending to API
        results = []
        for _, row in df.iterrows():
            json_data = row.to_json()
            result = send_json(json_data)
            results.append(result)
        # Display results
        for result in results:
            st.json(result)

if __name__ == "__main__":
    app()
