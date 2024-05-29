import os

HIGHSCORE_FILE = "highscores.txt"

def load_high_score():
    if not os.path.exists(HIGHSCORE_FILE):
        return 0
    with open(HIGHSCORE_FILE, 'r') as file:
        return int(file.readline().strip())

def save_high_score(score):
    with open(HIGHSCORE_FILE, 'w') as file:
        file.write(str(score))

def load_high_scores():
    if not os.path.exists(HIGHSCORE_FILE):
        return []
    with open(HIGHSCORE_FILE, 'r') as file:
        return [int(line.strip()) for line in file.readlines()]

def save_high_scores(scores):
    with open(HIGHSCORE_FILE, 'w') as file:
        for score in scores:
            file.write(f"{score}\n")
