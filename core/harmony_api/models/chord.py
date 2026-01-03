from pydantic import BaseModel

class Chord(BaseModel):
    name: str
    start: float
    end: float
