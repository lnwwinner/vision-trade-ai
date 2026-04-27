import subprocess
import cv2
import numpy as np


def capture_screen():
    result = subprocess.run([
        "adb", "exec-out", "screencap", "-p"
    ], stdout=subprocess.PIPE)

    img = np.frombuffer(result.stdout, np.uint8)
    frame = cv2.imdecode(img, cv2.IMREAD_COLOR)
    return frame
