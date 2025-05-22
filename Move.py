directions = ["north", "south", "east", "west"]

def move():
    while True:
        print("Which way do you want to go?")
        for i in range(0, 4):
            print(f"{i+1}. {directions[i]}")
        choice = int(input("choice (a number from 1 to 4): "))
        if choice > 0 and choice <= 4:
            return choice-1
        else:
            print("Please choose a number between 1 and 4, inclusive.")