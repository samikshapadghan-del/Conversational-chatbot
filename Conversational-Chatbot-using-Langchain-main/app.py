import os
import streamlit as st
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Conversational Chatbot", page_icon=":earth_americas:")
st.header("Hey, Lets Chat!")

chat = ChatGroq(temperature=0.5, model_name="llama-3.3-70b-versatile", groq_api_key=os.environ["GROQ_API_KEY"])

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [
        SystemMessage(content="Hello, I am a chatbot. I am here to help you with your queries. Please ask me anything!")
    ]

def get_response(query):
    st.session_state['flowmessages'].append(HumanMessage(content=query))
    answer = chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content

input = st.text_input("Input: ", key="input")
submit = st.button("Submit")

if submit and input:
    response = get_response(input)
    st.write(response)
