from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Chord(BaseModel):
    name: str
    start: float
    end: float

class VideoRequest(BaseModel):
    url: str

class ChordResponse(BaseModel):
    chords: List[Chord]

@app.post("/extract_chords", response_model=ChordResponse)
def extract_chords(request: VideoRequest):
    # TODO: Implement YouTube video processing and chord extraction
    # Example response
    example_chords = [
        Chord(name="C", start=0.0, end=2.5),
        Chord(name="G", start=2.5, end=5.0),
        Chord(name="Am", start=5.0, end=7.5)
    ]
    return ChordResponse(chords=example_chords)
