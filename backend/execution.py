import subprocess


def tap(x, y):
    subprocess.run(["adb", "shell", "input", "tap", str(x), str(y)])


def execute(action):
    if action == "BUY":
        tap(900, 1800)
    elif action == "SELL":
        tap(200, 1800)
