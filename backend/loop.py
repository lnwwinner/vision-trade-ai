from backend.capture import capture_screen
from backend.vision import analyze_frame
from backend.decision import decide
from backend.execution import execute
import time


def run_loop():
    print("Starting AI Trading Loop...")
    while True:
        frame = capture_screen()

        result = analyze_frame(frame)
        action = decide(result['signal'], result['confidence'])

        print(f"Signal: {result['signal']} | Confidence: {result['confidence']} | Action: {action}")

        if action != "WAIT":
            execute(action)

        time.sleep(5)


if __name__ == "__main__":
    run_loop()
