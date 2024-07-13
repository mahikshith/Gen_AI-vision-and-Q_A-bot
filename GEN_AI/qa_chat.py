from dotenv import load_dotenv 
load_dotenv()
# load the  variables defined in env 

import streamlit as st 
import os 
import google.generativeai as genai 

##Check this out for google api documentation reference : 
## https://colab.research.google.com/github/google/generative-ai-docs/blob/main/site/en/gemini-api/docs/get-started/python.ipynb#scrollTo=vm9tUYeT8lBc

# Api configure

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# func to load gemini api pro model for responses 
model = genai.GenerativeModel('gemini-pro') 
chat = model.start_chat(history=[])

def gemini_response(question): 
    answer = chat.send_message(question,stream=True)
    answer.resolve()
    return answer

# streamlit intialization AKA session state where it stores chat history

st.header("Gemini Q&A chat response application demo")

if 'chat_hist' not in st.session_state : 
    st.session_state['chat_hist'] = [] 

user_input = st.text_input("Enter your query:",key="user_input")
submit = st.button("Ask the question")

if submit and user_input : 
    answer = gemini_response(user_input)

# appending the OG input and then answer into the session history
    st.session_state['chat_hist'].append(("user",user_input))
    st.subheader("gemini's answer : ")
    for each_chunk in answer  :
        st.write(each_chunk.text)
        st.session_state['chat_hist'].append(('gemini',each_chunk.text))

# we need to display information 

st.subheader("Your chat history with gemini :") 

for role , txt in st.session_state['chat_hist']: 
    st.write(f"{role} : {txt}")


    
