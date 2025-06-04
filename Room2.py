import Bag as b

def room2():
    print("In this room, you only see a locked box with a four-digit password.")
    while True:
        choice = input("What do you do now?: ")
        if "bag" in choice.lower().split():
            while True:
                b.check()
                print("Which item do you want to use now?")
                ans = int(input("choose a number: "))
                if ans > 0 and ans <= len(b.bag):
                    if b.bag[ans-1] == "UV Torch":
                        print("Using the UV Torch, you see the hidden password: 3421.")
                        print("Hooray, you get the last piece of key fragment! You escape the hotel!")
                        print("Thank you for playing my game!")
                        break
                    else:
                        print("This item is not useful now. Please pick again.")
                else:
                    print("Pleae pick a number labeled in front of the items.")
            break
        else:
            print("Hint: type out the thing that you have along the way.")
        

