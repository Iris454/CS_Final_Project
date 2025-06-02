import Move as m
import Bag as b

def room2():
    print("In this room, you only see a locked box with a four-digit password.")
    choice = input("What do you do now?: ")
    if "bag" in choice.lower().split():
        b.check()
        
        

