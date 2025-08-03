from .. import schemas, models
from ..database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException
from typing import Optional
from .. config import settings
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import json
import time
import os

router = APIRouter(
    prefix="/ollama",
    tags=["Ollama"]
)

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path="/home/mahdi/Desktop/Langchain/.env")
langsmith_api_key = os.getenv("LANGSMITH_API_KEY")
if langsmith_api_key:
    os.environ["LANGSMITH_API_KEY"] = langsmith_api_key

langsmith_tracing = os.getenv("LANGSMITH_TRACING")
if langsmith_tracing:
    os.environ["LANGCHAIN_TRACING_V2"] = langsmith_tracing
llm = Ollama(
    model="llama2",
)

print("LangSmith key:", os.getenv("LANGSMITH_API_KEY"))
print("LangChain tracing V2:", os.getenv("LANGCHAIN_TRACING_V2"))



prompt1 = ChatPromptTemplate.from_template( "You are a poet. Write a poem about {topic}." )
prompt2 = ChatPromptTemplate.from_template( "You are a writer. Write a essay about {topic}." )

@router.post("/poem", status_code=status.HTTP_201_CREATED , response_model=schemas.OllamaResponse)
def create_poem(
   new_poem_request: schemas.OllamaRequest , db: Session = Depends(get_db)
):
    """
    Create a poem about the given topic using Ollama.
    """
    print(f"Starting poem generation for topic: {new_poem_request.topic}")
    start_time = time.time()
    
    chain = prompt1 | llm 
    print("Invoking Ollama model...")
    response = chain.invoke({"topic": new_poem_request.topic})
    
    generation_time = time.time() - start_time
    print(f"Poem generated in {generation_time:.2f} seconds")

    
    usage_info = {
        "model": "llama2", 
        "tokens": len(response.split()),
        "generation_time_seconds": round(generation_time, 2)
    }

    new_poem_response = models.Ollama_poem(
        topic=new_poem_request.topic,
        response=response,
        usage=json.dumps(usage_info)  
    )

    db.add(new_poem_response)
    db.commit()
    db.refresh(new_poem_response)

    return new_poem_response




@router.post("/essay", status_code=status.HTTP_201_CREATED , response_model=schemas.OllamaResponse)
def create_essay(
   new_essay_request: schemas.OllamaRequest , db: Session = Depends(get_db)
):
    """
    Create an essay about the given topic using Ollama.
    """
    print(f"Starting essay generation for topic: {new_essay_request.topic}")
    start_time = time.time()
    
    chain = prompt2 | llm 
    print("Invoking Ollama model...")
    response = chain.invoke({"topic": new_essay_request.topic})
    
    generation_time = time.time() - start_time
    print(f"Essay generated in {generation_time:.2f} seconds")

    usage_info = {
        "model": "llama2", 
        "tokens": len(response.split()),
        "generation_time_seconds": round(generation_time, 2)
    }

    new_essay_response = models.Ollama_essay(
        topic=new_essay_request.topic,
        response=response,
        usage=json.dumps(usage_info)  
    )

    db.add(new_essay_response)
    db.commit()
    db.refresh(new_essay_response)

    return new_essay_response