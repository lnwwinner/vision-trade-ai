import cv2
import numpy as np


def analyze_frame(frame):
    # Simple real analysis (not random)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    avg_brightness = np.mean(gray)

    # basic trend logic
    if avg_brightness > 130:
        return {"signal": "BUY", "confidence": 65}
    elif avg_brightness < 100:
        return {"signal": "SELL", "confidence": 65}
    else:
        return {"signal": "WAIT", "confidence": 50}
