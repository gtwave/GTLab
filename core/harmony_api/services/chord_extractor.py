# TODO: Implement actual chord extraction from YouTube video
from typing import List
from ..models.chord import Chord

def extract_chords_from_video(url: str) -> List[Chord]:
    # Placeholder implementation
    return [
        Chord(name="C", start=0.0, end=2.5),
        Chord(name="G", start=2.5, end=5.0),
        Chord(name="Am", start=5.0, end=7.5)
    ]
