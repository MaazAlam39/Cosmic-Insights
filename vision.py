from dotenv import load_dotenv
load_dotenv() ##loading all the environment variables

import os
import streamlit as st
import google.generativeai as genai 

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

model=genai.GenerativeModel("gemini-pro-vision")
def get_gemini_response(input,image):
    if input!="":
        response=model.generate_content([input,image])
    else:
        response=model.generate_content([image])   
    return response.text

#initialise streamlit app
st.set_page_config(page_title="Gemini Image") 
st.header("Gemini Appllication")
input=st.text_input("Input Prompt: ",key="input")
image=st.file_uploader("Upload Image",type=['png','jpg','jpeg'])
if image is not None:
    st.image(image,use_column_width=True)
    with st.expander("See Generated Text"):
        st.write(get_gemini_response(input,image))
else:
    st.write("Please upload an image")
        
submit=st.button("Generate")
if submit:
    response=get_gemini_response(input,image)
    st.subheader("The Response is:")
    st.write(response)
