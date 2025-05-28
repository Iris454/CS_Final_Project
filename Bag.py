from tabulate import tabulate

bag = []

def check():
    for idx in range(0, len(bag)):
        print(f"{idx+1}. {bag[idx]}")

first_floor = [[None, "elevator", None], ["lobby", "restuarant", "pool"]]
second_floor = [["elevator", "Room103", "Room104"], [None, "gym", None]]

def map():
    print("first floor:")
    print(tabulate(first_floor, tablefmt = "fancy_grid"))
    print("second floor:")
    print(tabulate(second_floor, tablefmt = "fancy_grid"))