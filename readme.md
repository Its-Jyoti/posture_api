🏗️ Project Architecture
posture_api/
│
├── app/
│   ├── main.py        # FastAPI entry point
│   ├── analysis.py    # State-based posture risk logic
│   ├── auth.py        # Dummy API key authentication
│   ├── dummy_data.py  # 1 FPS dummy posture data (Team-1 simulation)
│   ├── models.py     # Pydantic data models
│   └── database.py   # Database layer (SQLite for now)
│
├── posture.db         # Auto-created database file
├── requirements.txt
└── README.md
⚙️ Technologies Used

Python 3

FastAPI

Uvicorn

Pydantic

SQLite (temporary – will migrate to PostgreSQL)

🔐 API Authentication

All protected APIs require an API key.

Header

x-api-key: test-api-key-123
🚀 How to Run the Project
1️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run FastAPI Server
python -m uvicorn app.main:app --reload
4️⃣ Open Swagger UI
http://127.0.0.1:8000/docs
📡 Available APIs
✅ Health Check
GET /health

Response:

{ "status": "API is running" }
🧪 Get Dummy Session Data (Team-1 Simulation)
GET /session/dummy

Generates dynamic posture frames

1 FPS (1 frame = 1 second)

Includes angle + confidence for neck, shoulder, torso, head

🧠 Analyze Posture Session (Team-2 Logic)
POST /session/analyze

Input:
Full session JSON (output of /session/dummy)

Output Example:

{
  "metric": "neck",
  "final_verdict": "WARNING",
  "risk_level": "MODERATE",
  "state_time_minutes": {
    "GOOD": 0.83,
    "WARNING": 0.67,
    "BAD": 0.5
  },
  "reason": "State-based posture risk analysis",
  "recommended_action": "Posture correction and scheduled breaks"
}