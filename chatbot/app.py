from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path="../.env")

# Check and set environment variables with error handling
openai_api_key = os.getenv("OPENAI_API_KEY")
if openai_api_key:
    os.environ["OPENAI_API_KEY"] = openai_api_key
else:
    st.error("OPENAI_API_KEY not found. Please set it in your .env file or environment variables.")
    st.stop()

#langsmith tracing (optional)
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

##streamlit app
st.title("Langchain Chatbot")

question = st.text_input("Ask a question:")

#openAi LLM
llm = ChatOpenAI(
    model="gpt-3.5-turbo",

)
#output parser
output_parser = StrOutputParser()

#chain
chain = prompt | llm | output_parser

if question:
    with st.spinner("Thinking..."):
        response = chain.invoke({"question": question})
        st.write(response)

