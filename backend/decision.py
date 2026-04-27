def decide(signal, confidence):
    if confidence > 70:
        return signal
    return "WAIT"
