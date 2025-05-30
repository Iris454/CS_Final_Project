import Bag as b
import Room1 as r

def elevator():
    print("Ding! The elevator is here." \
        "You move up to the second floor.")
    print("The door is open. You walk out of the elevator. " \
        "Room103 is right in front of you, but it's locked." \
        "What do you do now?")
    while True:
        print("1. go over the items in your bag")
        print("2. keep walking")
        choice = int(input("choice (1/2): "))
        if choice == 1:
            while True:
                b.check()
                print("Which item do you want to use now?")
                ans = int(input("choose a number: "))
                if ans > 0 and ans <= len(b.bag):
                    if b.bag[ans-1] == "Room103 Key":
                        print("You use the key to unlock the door.")
                        r.room1()
                        break
                    else:
                        print("This item is not useful now. Please pick again.")
                else:
                    print("Pleae pick a number labeled in front of the items.")
            break
        elif choice == 2:
            print("All the doors are locked. You can't go anywhere. Please choose again.")
        else:
            print("Please choose 1 or 2.")

    
