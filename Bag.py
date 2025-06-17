bag = []

def check(): # allow the player to go over all the items in the bag
    for idx in range(0, len(bag)):
        print(f"{idx+1}. {bag[idx]}")
