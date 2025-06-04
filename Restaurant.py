import Move as m
import Elevator as e
import Pool as p
import Bag as b
eat = True
flag = True

def north():
    global flag
    print("That way is the elevator.")
    if eat:
        print("Please visit other places first before leaving the restuarant in elevator.")
    else:
        while True:
            print("To go into the elevator you have to solve this easy riddle!")
            print("I have keys, but no locks, I have a space, but no room. You can enter, but can't go outside.")
            answer = input("What am I?: ")
            if answer == "keyboard" or "Keyboard": 
                print("Congratulations, you have solved it, very intelligent.")
                flag = False
                e.elevator()
                break
            else:
                print("No, that is wrong.")


def south():
    print("Under a table, you find a purple UV Torch. You collect it.")
    b.bag.append("UV Torch")

def east():
    global eat
    while True:
        print("That's the pool, to go there you have to solve this tricky riddle!")
        print("Tim's mom has 4 sons, Red, Orange, and Yellow.")
        answer = input("What is the fourth son's name?: ")
        if answer == "Tim":
            print("Yes, you're clever. Now you can go into the pool.")
            eat = False
            p.Pool()
            break
        else:
            print("Wrong.")


def west():
    print("You've already collected everything from the lobby, you don't need to go that way.")

dir = [north, south, east, west]

def restaurant():
    while flag:
        direction = m.move()
        dir[direction]()
