from dotenv import load_dotenv 
load_dotenv()
# loaded the env variables 
import streamlit as st 
import os 
import google.generativeai as genai 

'''Check this out for google api documentation reference : 
https://colab.research.google.com/github/google/generative-ai-docs/blob/main/site/en/gemini-api/docs/get-started/python.ipynb#scrollTo=vm9tUYeT8lBc
'''
# Api configure

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# func to load gemini api pro model for responses 

def gemini_response(question): 
    model = genai.GenerativeModel('gemini-pro') 
    answer = model.generate_content(question)
    return answer.text

# streamlit-- intialize 

st.header("Gemini response application demo")

user_input = st.text_input("Enter your query:",key="user_input")

submit = st.button("Ask the question")

if submit:
  response = gemini_response(user_input)
  st.subheader("Gemini's response is:")
  st.write(response)

