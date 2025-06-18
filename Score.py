import Search as s
import Info as i

highScoreFile = "SplunkingHighScore.txt"

highScore = 0

def getHighScore():
    global highScore
try:
    with open(highScoreFile, 'r') as file:
        highScore = int(file.read())
 except:
      with open(highScoreFile, ‘w’) as file:
             file.write(‘0’)
      highScore = 0

def newHighScore(newScore):
    with open(highScoreFile, 'w') as file:
        file.write(newScore)


def evaluate_loot():
    score = 0
    print("You found the following items: ")
    for item in i.diver["bag"]["inventory"]:
        print(f" - {s.items[item]['name']} ({s.items[item]['value']})")
        score += s.items[item]["value"]
    return score

def calculate_score():
    i.diver["score"] = evaluate_loot()
    print(f"Total value of your loot: {i.diver['score']}")
    print(f"Current high score: {highScore}")
    if i.diver["score"] > int(highScore):
        newHighScore(str(i.diver["score"]))
        print(f"New high score: {i.diver['score']}")
    else:
        print("better luck next time.")

