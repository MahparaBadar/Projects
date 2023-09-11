import streamlit as st
from transformers import AutoModel
import requests

# Define your Seamless M4T API token
api_token = "Actual API Token"

# Streamlit app layout
st.title("Mahpara's Multilingual Chatterbox")

# Text input for user to enter text
user_input = st.text_area("Enter text:", "The goal of life is...")

# Language selection for source and target
source_language = st.selectbox("Select source language:", ["en", "fr", "es", "de"])  # Add more languages as needed
target_language = st.selectbox("Select target language:", ["en", "fr", "es", "de"])  # Add more languages as needed

# Button to initiate translation
if st.button("Translate"):
    # Define the API endpoint
    api_url = "https://api.seamlessm4t.com"

    # Set headers with the API token
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
    }

    # Create the payload with the user's text and selected languages
    payload = {
        "text": user_input,
        "source_language": source_language,
        "target_language": target_language,
        "task": "tts",  # Set the task to text-to-speech
    }

    # Send a POST request to the Seamless M4T API
    response = requests.post(api_url, headers=headers, json=payload)
    



    if response.status_code == 200:
        audio_url = response.json()["audio_url"]
        st.audio(audio_url, format="audio/wav")
    else:
        st.write("Translation to speech failed. Please try again.")

