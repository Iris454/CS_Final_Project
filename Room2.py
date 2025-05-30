import Move as m
from tabulate import tabulate
password = "042"

def north():
    pass

def south():
    pass

def east():
    print("You see a locked box. The password is three-digit.")
    print("On a piece of paper next to the box, you see:")
    grid = [[6, 8, 2, "One number is correct and well placed"],
            [6, 1, 4, "One number is correct but wrong placed"],
            [2, 0, 6, "Two numbers are correct but wrong placed"],
            [7, 3, 8, "Nothing is correct"],
            [7, 8, 0, "One number is correct but wrong placed"]]
    print(tabulate(grid, tablefmt = "fancy_grid"))

    ans = input("Password (type three numbers in the correct order without spaces): ")
    if ans == password:
        pass
    else:
        print("Wrong password. Please try again.") 

def west():
    pass

dir = [north, south, east, west]

def room2():
    direction = m.move()
    dir[direction]()
