from pydantic import BaseModel
from typing import List

# FastAPI 응답 모델
class TopArtist(BaseModel):
    ArtistName: str
    TrackCount: int