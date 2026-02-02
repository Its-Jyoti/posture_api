from fastapi import FastAPI, Depends
from fastapi import Body
from .analysis import analyze_neck_session
from .auth import verify_api_key
from .dummy_data import get_dummy_session_data
from .models import SessionData

app = FastAPI(
    title="Posture Dummy API",
    description="Simulates posture data for pain risk analysis",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    return {"status": "API is running"}

@app.get(
    "/session/dummy",
    response_model=SessionData,
    dependencies=[Depends(verify_api_key)]
)
def get_dummy_session():
    return get_dummy_session_data()

@app.post(
    "/session/analyze",
    dependencies=[Depends(verify_api_key)]
)
def analyze_session(session: SessionData = Body(...)):
    return analyze_neck_session(session.frames)