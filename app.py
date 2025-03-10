import streamlit as st
import google.generativeai as genai


API_KEY = st.secrets["GEMINI_API_KEY"] 

genai.configure(api_key=API_KEY)
# Initialize the model
model = genai.GenerativeModel("gemini-2.0-flash")

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
