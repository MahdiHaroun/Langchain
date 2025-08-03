from pydantic import BaseModel, field_validator
from datetime import datetime
import json
from typing import Union


class OllamaResponse(BaseModel):
    id: int
    created_at: datetime
    topic: str
    response: str
    usage: dict
    
    @field_validator('usage', mode='before')
    @classmethod
    def parse_usage(cls, v):
        if isinstance(v, str):
            return json.loads(v)
        return v

    class Config:
        from_attributes = True


class OllamaRequest(BaseModel):
    topic: str



