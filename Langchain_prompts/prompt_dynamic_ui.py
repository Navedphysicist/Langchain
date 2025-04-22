from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

from langchain_core.prompts import PromptTemplate

load_dotenv()

st.header('Cricket Research Tool')

team_input = st.selectbox('Select the team for your research: ',['India','Austrailia','Bangladesh','New Zealand'])

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented"])

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )


# load_prompt('template.json')

model  = ChatOpenAI(model='gpt-4o',temperature=0)

template  = PromptTemplate(
 template="""
        Please summarize the Cricket research paper titled "{team_input}" with the following specifications:
        Explanation Style: {style_input}  
        Explanation Length: {length_input}   
        2. Analogies:  
        - Use relatable analogies to simplify complex ideas.    
        Ensure the summary is clear, accurate, and aligned with the provided style and length.
   """,
   input_variables=['team_input','style_input','length_input']
)

prompt = template.invoke({
    'team_input': team_input,
    'style_input': style_input,
    'length_input':length_input
})

if st.button('Summarize'):
    result = model.invoke(prompt)
    st.write(result.content)
