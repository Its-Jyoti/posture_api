# app/analysis.py

CONFIDENCE_THRESHOLD = 0.80
FPS = 1  # 1 frame = 1 second


def classify_neck_state(angle: float) -> str:
    if 0 <= angle <= 10:
        return "GOOD"
    elif 11 <= angle <= 30:
        return "WARNING"
    else:
        return "BAD"


def exposure_label(time_minutes: float) -> str:
    if time_minutes <= 5:
        return "TRANSIENT"
    elif time_minutes <= 15:
        return "SHORT"
    elif time_minutes <= 30:
        return "SUSTAINED"
    else:
        return "PROLONGED"


ESCALATION_MATRIX = {
    ("GOOD", "TRANSIENT"): "GOOD",
    ("GOOD", "SHORT"): "GOOD",
    ("GOOD", "SUSTAINED"): "GOOD",
    ("GOOD", "PROLONGED"): "WARNING",

    ("WARNING", "TRANSIENT"): "WARNING",
    ("WARNING", "SHORT"): "WARNING",
    ("WARNING", "SUSTAINED"): "BAD",
    ("WARNING", "PROLONGED"): "BAD",

    ("BAD", "TRANSIENT"): "WARNING",
    ("BAD", "SHORT"): "WARNING",
    ("BAD", "SUSTAINED"): "BAD",
    ("BAD", "PROLONGED"): "BAD",
}


def analyze_neck_session(frames: list) -> dict:
    state_time_seconds = {"GOOD": 0, "WARNING": 0, "BAD": 0}

    for frame in frames:
        neck = frame.neck          # ✅ object access
        angle = neck.angle
        confidence = neck.confidence

        if confidence < CONFIDENCE_THRESHOLD:
            continue

        state = classify_neck_state(angle)
        state_time_seconds[state] += 1  # 1 FPS = 1 second

    # convert seconds → minutes
    state_time_minutes = {
        state: round(seconds / 60, 2)
        for state, seconds in state_time_seconds.items()
    }

    escalated_states = {}

    for state, time_min in state_time_minutes.items():
        if time_min == 0:
            continue
        exposure = exposure_label(time_min)
        escalated_states[state] = ESCALATION_MATRIX[(state, exposure)]

    # dominance rules
    if "BAD" in escalated_states.values():
        verdict = "BAD"
        risk = "HIGH"
    elif "WARNING" in escalated_states.values():
        verdict = "WARNING"
        risk = "MODERATE"
    else:
        verdict = "GOOD"
        risk = "LOW"

    return {
        "metric": "neck",
        "final_verdict": verdict,
        "risk_level": risk,
        "state_time_minutes": state_time_minutes,
        "reason": "State-based posture risk analysis",
        "recommended_action": (
            "Posture correction and scheduled breaks"
            if verdict != "GOOD"
            else "Maintain posture"
        )
    }