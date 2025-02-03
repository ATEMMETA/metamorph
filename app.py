import streamlit as st
import requests

Set up the backend API endpoint
api_endpoint = "http://localhost:5000/api/messages"

Create a Streamlit application
st.title("MetaHub")

Create a text input for the user to enter a message
user_input = st.text_input("Enter a message")

Create a button to send the message to the backend API
if st.button("Send"):
    # Send the message to the backend API
    response = requests.post(api_endpoint, json={"message": user_input})
    
    # Display the response from the backend API
    st.write(response.json())
