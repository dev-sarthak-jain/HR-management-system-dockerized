import streamlit as st
import pandas as pd
import requests

# Function to send JSON to API and get predictions
def send_json(data, url="http://127.0.0.1:8000/api/employee_create/"):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)
    return response.json()

def app():
    st.title('Employee Attrition Prediction App')
    
    # File uploader widget
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=['csv'])
    st.text_input("enter","uggyf")

    if uploaded_file is not None:
        # Reading the uploaded CSV file
        df = pd.read_csv(uploaded_file)
        
        # Converting each row to JSON and sending to API
        json_data = df.to_dict(orient='records')  # Convert DataFrame to list of dicts
        results = send_json(json_data)

        # Display results
        if results:
            # Convert results back to DataFrame to display in a table format
            results_df = pd.DataFrame(results)
            # Transforming prediction output
            print(results_df['attrition prediction'])
            results_df['attrition prediction'] = results_df['attrition prediction'].apply(lambda x: 'High Chances' if x[0] == 1 else 'Low Chances')
            
            st.dataframe(results_df)  # Displaying the modified DataFrame
        else:
            st.write("No results to display.")

if __name__ == "__main__":
    app()
