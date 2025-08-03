from .database import Base 
from sqlalchemy import Column, Integer, String, Boolean , ForeignKey 
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql import text
from sqlalchemy.orm import relationship


class Ollama_poem(Base):
    __tablename__ = "ollama_poems"

    id = Column(Integer, primary_key=True, nullable=False)
    topic = Column(String, nullable=False)
    response = Column(String, nullable=False)
    usage = Column(String, nullable=False)  
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))



class Ollama_essay(Base):
    __tablename__ = "ollama_essays"

    id = Column(Integer, primary_key=True, nullable=False)
    topic = Column(String, nullable=False)
    response = Column(String, nullable=False)
    usage = Column(String, nullable=False)  
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))