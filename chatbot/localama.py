from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import ollama


import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path="../.env")
langsmith_api_key = os.getenv("LANGSMITH_API_KEY")
if langsmith_api_key:
    os.environ["LANGCHAIN_API_KEY"] = langsmith_api_key

langsmith_tracing = os.getenv("LANGSMITH_TRACING")
if langsmith_tracing:
    os.environ["LANGCHAIN_TRACING_V2"] = langsmith_tracing

##prompt template 

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant . Please answer the following question."),
        ("user", "{question}")
    ]
)

st.title("Langchain Chatbot with Ollama")

question = st.text_input("Ask a question:")

#Ollama LLM
llm = ollama.Ollama(
    model="llama2",
)

#output parser
output_parser = StrOutputParser()

#chain
chain = prompt | llm | output_parser

if question:
    with st.spinner("Thinking..."):
        response = chain.invoke({"question": question})
        st.write(response)