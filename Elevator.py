import Bag as b
import Room1 as r
import Countdown as c

def elevator():
    print()
    c.countdown(2)
    print("Ding! The elevator is here. \n"
        "You move up to the second floor.")
    print("The floor creeks of the old elevator, there are only 2 buttons,"\
          " 1 and 2. Be carefull, it might break down.")
    print("The door is open. You walk out of the elevator.  \n" 
        "Room103 is right in front of you, but it's locked.  \n"
        "What do you do now?")

    while True:
        try:
            print("1. go over the items in your bag")
            print("2. keep walking")
            choice = int(input("choice (1/2): "))
            if choice == 1:
                while True:
                    try:
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
                    except:
                        print("Please type a number.")
                break
            elif choice == 2:
                print("All the doors are locked. You can't go anywhere. Please choose again.")
            else:
                print("Please choose 1 or 2.")
        except:
            print("Please type a number.")

    
