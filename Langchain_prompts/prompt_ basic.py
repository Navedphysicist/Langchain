from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
load_dotenv()


st.header('Cricket Research Tool')
model  = ChatOpenAI(model='gpt-4o',temperature=0)



user_input = st.text_input('Enter your prompt')

if st.button('Summarize'):
    result = model.invoke(user_input)
    st.text(result.content)


