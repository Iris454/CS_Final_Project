directions = ["north", "south", "east", "west"]    # a list of directions

'''
a move function that asks the player to choose which direction they want to go
and returns a number between 0 and 4, with each number corresponds to a direction
'''
def move():
    print()
    print("Which way do you want to go?")
    while True:
        try:
            for i in range(0, 4):
                print(f"{i+1}. {directions[i]}")
            choice = int(input("choice (a number from 1 to 4): "))
            if choice > 0 and choice <= 4:
                return choice-1 # returns a number between 0 and 4
            else:
                print("Please choose a number between 1 and 4, inclusive.")
        except:
            print("Please type a number.")