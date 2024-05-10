import streamlit as st
import pandas as pd
import requests

# Function to send JSON to API and get predictions
def send_json(data, url="http://127.0.0.1:8000/api/employee_create/"):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)
    return response

def app():
    st.title('Employee Attrition Prediction App')
    
    # File uploader widget in the sidebar
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=['csv'])

    # Creating containers
    top_container = st.container()  # This will be the top part for text input
    bottom_container = st.container()  # This will be for the output column

    # Text input at the top of the page
    with top_container:
        st.text_input("", placeholder="Enter your query here", key='query_input')

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        json_data = df.to_dict(orient='records')  # Convert DataFrame to list of dicts
        response = send_json(json_data)
        if response.status_code == 200:
            st.success("Data successfully sent to API")
            with bottom_container:
                st.write(response.text)  # Display the API response
        else:
            st.error("Failed to send data to API")

if __name__ == "__main__":
    app()