import Move as m

def north():
    print("That's the elevator, to go there you have to solve this easy riddle!")
    print("I have keys, but no locks, I have a space, but no room. You can enter, but can't go outside.")
    answer = input("What am I?: ")
    if answer == "keyboard" or "Keyboard": 
    print("Congratulations, you have solved it, very intelligent.")
    else:
    print("No, that is wrong.")


def south():
    print("Sorry there's nothing that way, pick another direction.")

def east():
    print("That's the pool, to go there you have to solve this tricky riddle!")
    print("Tim's mom has 4 sons, Red, Orange, and Yellow.")
    answer = input("What is the fourth son's name?: ")
    if answer == "Tim":
        print("Yes, you're clever. Now you can go into the pool.")
    else:
        print("Wrong.")
    

def west():
    print("You're back in the lobby")

dir = [north, south, east, west]

def restaurant():
    direction = m.move()
    dir[direction]()
    
