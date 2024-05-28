HIGH_SCORE_FILE = "high_scores.txt"

def save_high_score(score):
    high_score = load_high_score()
    if score > high_score:
        with open(HIGH_SCORE_FILE, "w") as file:
            file.write(str(score))

def load_high_score():
    try:
        with open(HIGH_SCORE_FILE, "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0
