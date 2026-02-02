from pydantic import BaseModel
from typing import List


class AngleConfidence(BaseModel):
    angle: float
    confidence: float


class Frame(BaseModel):
    frame_index: int
    neck: AngleConfidence
    shoulder: AngleConfidence
    torso: AngleConfidence
    head: AngleConfidence


class SessionData(BaseModel):
    session_id: str
    fps: int
    frames: List[Frame]