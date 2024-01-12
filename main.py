# main_app.py
from dotenv import load_dotenv
load_dotenv() ##loading all the environment variables

import os
import streamlit as st
import google.generativeai as genai 
from streamlit.hashing import _CodeHasher

# genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Function to set custom styles

def set_custom_style():
    custom_css = """
        body {
            background-color: #f4f4f4;
            color: #333;
            font-family: 'Roboto', sans-serif;
        }
        .stApp {
            max-width: 1200px;
            margin: 0 auto;
        }
        """
    st.markdown(f'<style>{custom_css}</style>', unsafe_allow_html=True)

# Function to load Gemini Pro Vision model

def load_gemini_model():
    genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
    return genai.GenerativeModel("gemini-pro-vision")

# Function to generate Gemini response
def get_gemini_response(model, input_text, image):
    if input_text != "":
        response = model.generate_content([input_text, image])
    else:
        response = model.generate_content([image])
    return response.text

# Main function for Streamlit app
def main():
    set_custom_style()
    st.set_page_config(page_title="Gemini Image")

    st.title("Gemini Application")

    page = st.sidebar.selectbox("Select a page", ["App 1", "App 2"])

    if page == "App 1":
        # Your App 1 content here
        input_app1 = st.text_input("Input Prompt for App 1: ", key="input_app1")
        image_app1 = st.file_uploader("Upload Image for App 1", type=['png', 'jpg', 'jpeg'])
        if image_app1 is not None:
            st.image(image_app1, use_column_width=True)
            with st.expander("See Generated Text for App 1"):
                st.write(get_gemini_response(model, input_app1, image_app1))
        else:
            st.write("Please upload an image for App 1")

    elif page == "App 2":
        # Your App 2 content here
        input_app2 = st.text_input("Input Prompt for App 2: ", key="input_app2")
        if image_app2 is not None:
            st.image(image_app2, use_column_width=True)
            with st.expander("See Generated Text for App 2"):
                st.write(get_gemini_response(model, input_app2, image_app2))
           
if __name__ == '__main__':
    main()
