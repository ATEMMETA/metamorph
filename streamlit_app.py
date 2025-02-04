import streamlit as st

# Create a title for the app
st.title("AI API Connector")

# Create a text input for API key
api_key = st.text_input("Enter API Key", type="password")  # Mask the API key for security

# Create a dropdown menu for API selection
api_options = ["Gemini API", "Our AI API"]
selected_api = st.selectbox("Select API", api_options)

# Create a text input for Gemini API chat. Use a text area for longer conversations.
gemini_chat = st.text_area("Gemini API Chat", height=150)  # Adjust height as needed

# Create a text input for Our AI chat. Use a text area for longer conversations.
our_ai_chat = st.text_area("Our AI Chat", height=150)  # Adjust height as needed

# Create a status indicator. Initialize as disconnected.  Define it *before* the button.
status = st.text("Status: Disconnected")


# Create a button to connect/disconnect API
if st.button("Connect/Disconnect API"):
    if api_key:  # Check if an API key is entered
        if selected_api == "Gemini API":
            # Add code here to connect/disconnect Gemini API using the api_key and gemini_chat
            st.write(f"Connecting to Gemini API with key: {api_key[:5]}... (Partially shown for security)")  # Display first few characters for confirmation
            # ... your Gemini API interaction code ...
            status.text("Status: Connected to Gemini API")  # Update the status
        elif selected_api == "Our AI API":
            # Add code here to connect/disconnect Our AI API using the api_key and our_ai_chat
            st.write(f"Connecting to Our AI API with key: {api_key[:5]}... (Partially shown for security)")  # Display first few characters for confirmation
            # ... your Our AI API interaction code ...
            status.text("Status: Connected to Our AI API")  # Update the status
    else:
        st.warning("Please enter an API key.")


import streamlit as st
import requests

if st.button("Get Data"):  # Button to trigger the API call
    try:
        response = requests.get("http://localhost:8000/data")
        response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)
        data = response.json()
        st.write(data)
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")  # Display the error message in Streamlit
        st.write("Failed to retrieve data. Check the error message above.")

