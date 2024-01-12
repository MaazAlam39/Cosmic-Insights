from dotenv import load_dotenv
load_dotenv() ##loading all the environment variables

import os
import streamlit as st
import google.generativeai as genai 


genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

##function to load Gemini Pro model
model=genai.GenerativeModel("gemini-pro")
# def load_gemini_pro_model():
#     return genai.load_model("gemini-pro")

def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

st.set_page_config(page_title="Q&A ")
st.header("The most advanced AI assistant")
# st.subheader("Ask any question and get answers instantly")

input=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

if submit:
    response=get_gemini_response(input)
    st.subheader("The Response is:")
    st.write(response)
