class SimpleLearner:
    def __init__(self):
        self.history = []

    def log(self, signal, result):
        self.history.append((signal, result))

    def stats(self):
        wins = sum(1 for s,r in self.history if r == 'WIN')
        total = len(self.history)
        return wins, total
