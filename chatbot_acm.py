from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ['LANGCHAIN_TRACKING_V2'] = 'true'
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user's queries"),
        ("user", "Question: {question}")
    ]
)

st.title('Chatbot ACM Inductions')
input_text = st.text_input("Search the topic you want:")

try:
    
    llm = Ollama(base_url='http://localhost:11434', model="llama3.1")
    output_parser = StrOutputParser()

    if input_text:

        formatted_prompt = prompt.format(question=input_text)
        
        response = llm(formatted_prompt)
        
        output = output_parser.parse(response)
        
        st.write(output)

except Exception as e:
    st.error(f"An error occurred: {e}")

