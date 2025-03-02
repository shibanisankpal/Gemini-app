import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")


# Initialize the model
model = genai.GenerativeModel("gemini-pro")

def generate_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.title("Gemini AI Chatbot")
st.write("Enter a prompt below and get a response from Google's Gemini AI.")

# User input
user_input = st.text_area("Your Prompt:")

if st.button("Generate Response"):
    if user_input:
        with st.spinner("Generating response..."):
            response = generate_response(user_input)
            st.subheader("Response:")
            st.write(response)
    else:
        st.warning("Please enter a prompt.")
