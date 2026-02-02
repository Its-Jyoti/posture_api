import random

FPS = 1  # 1 frame = 1 second


def get_dummy_session_data(session_duration_seconds: int = 120):
    """
    Generates dynamic dummy posture data at 1 FPS.
    Default session: 120 seconds (2 minutes)
    """

    frames = []
    frame_index = 1

    # ---- Block 1: WARNING posture (40 seconds) ----
    for _ in range(40):
        frames.append({
            "frame_index": frame_index,
            "neck": {"angle": 18, "confidence": round(random.uniform(0.85, 0.98), 2)},
            "shoulder": {"angle": 20, "confidence": round(random.uniform(0.85, 0.98), 2)},
            "torso": {"angle": 12, "confidence": round(random.uniform(0.85, 0.98), 2)},
            "head": {"angle": 15, "confidence": round(random.uniform(0.85, 0.98), 2)}
        })
        frame_index += 1

    # ---- Block 2: BAD posture (30 seconds) ----
    for _ in range(30):
        frames.append({
            "frame_index": frame_index,
            "neck": {"angle": 35, "confidence": round(random.uniform(0.85, 0.98), 2)},
            "shoulder": {"angle": 30, "confidence": round(random.uniform(0.85, 0.98), 2)},
            "torso": {"angle": 22, "confidence": round(random.uniform(0.85, 0.98), 2)},
            "head": {"angle": 28, "confidence": round(random.uniform(0.85, 0.98), 2)}
        })
        frame_index += 1

    # ---- Block 3: GOOD posture (remaining time) ----
    remaining = session_duration_seconds - len(frames)

    for _ in range(remaining):
        frames.append({
            "frame_index": frame_index,
            "neck": {"angle": 8, "confidence": round(random.uniform(0.90, 0.99), 2)},
            "shoulder": {"angle": 12, "confidence": round(random.uniform(0.90, 0.99), 2)},
            "torso": {"angle": 6, "confidence": round(random.uniform(0.90, 0.99), 2)},
            "head": {"angle": 9, "confidence": round(random.uniform(0.90, 0.99), 2)}
        })
        frame_index += 1

    return {
        "session_id": "DYNAMIC_DUMMY_SESSION_001",
        "fps": FPS,
        "frames": frames
    }