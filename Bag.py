from tabulate import tabulate

bag = []


first_floor = [[None, "elevator", None], ["lobby", "restuarant", "pool"]]
second_floor = [["elevator", "Room103", "Room104"], [None, "gym", None]]

def map():
    print("first floor:")
    print(tabulate(first_floor, tablefmt = "fancy_grid"))
    print("second floor:")
    print(tabulate(second_floor, tablefmt = "fancy_grid"))