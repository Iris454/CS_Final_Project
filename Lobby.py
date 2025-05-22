import Move as m

def north():
    pass

def south():
    pass

def east():
    pass

def west():
    pass

dir = [north, south, east, west]

def lobby():
    direction = m.move()
    dir[direction]()
    
