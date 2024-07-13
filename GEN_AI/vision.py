from dotenv import load_dotenv 
load_dotenv()

# loaded the env variables 
import streamlit as st 
import os 
import google.generativeai as genai 
from PIL import Image

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# func to load gemini api vison pro model for responses 

def gemini_response(question,image): 
    model = genai.GenerativeModel('gemini-pro-vision')

    if question!="":
        answer = model.generate_content([question,image],stream=True)
    else : 
        answer = model.generate_content(image)

    answer.resolve()
    return answer.text

'''Check this out for google api documentation reference : 
https://colab.research.google.com/github/google/generative-ai-docs/blob/main/site/en/gemini-api/docs/get-started/python.ipynb#scrollTo=vm9tUYeT8lBc
'''
      
# Don't forget that inpout should be in str format!!!

# streamlit initialization

st.header("Gemini's Image-text demo app")
input=st.text_input("Input Prompt: ",key="input")
input = str(input)

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Tell me about the image")

## If submit is clicked then

if submit:
    
    response=gemini_response(input,image)
    st.subheader("Gemini's Response is : ")
    st.write(response)
