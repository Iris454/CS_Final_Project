import Move as m
import Elevator as e
import Pool as p
import Bag as b
eat = True
flag = True

def north():
    global flag
    print("That way is the elevator.")
    if eat or "UV Torch" not in b.bag:
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
            p.pool()
            break
        else:
            print("Wrong.")


def west():
    print("You've already collected everything from the lobby, you don't need to go that way.")

dir = [north, south, east, west]

def restaurant():
    print("Now you are in the restuarant.")
    print("The lights are dim, shadows across the open space where tables are neatly arranged." \
            " Each set with folded napkins, polished dishes, and cutlery, prepared, but untouched." \
            " A crystal chandelier sways gently in a draft that seems to come from nowhere," \
            " though not a single window is open. The room is silent.")
    while flag:
        direction = m.move()
        dir[direction]()
