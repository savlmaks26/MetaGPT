import json

class Scoreboard:
    def __init__(self, file: str = 'scores.json'):
        self.file = file
        self.scores = []

    def load_scores(self):
        try:
            with open(self.file, 'r') as f:
                self.scores = json.load(f)
        except FileNotFoundError:
            self.scores = []

    def save_scores(self):
        with open(self.file, 'w') as f:
            json.dump(self.scores, f)

    def update_score(self, score: int):
        self.scores.append(score)
        self.scores.sort(reverse=True)
        self.scores = self.scores[:10]  # Keep only top 10 scores
