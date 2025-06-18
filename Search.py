import random
Import Info as i

items = {"rock": {"name": "rock", "description": "ordinary rock",
                  "value": 0},
         "silverCoin": {"name": "silver coin", "description":
                        "tarnished silver coin","value": 2},
         "goldCoin": {"name": "gold coin", "description": "shiny gold coin",
                      "value": 3},
         "ruby": {"name": "ruby", "description": "beautiful red ruby",
                  "value": 5}}
# List to represent items rarity.
rarity = ["rock", "rock", "silverCoin", "silverCoin", "silverCoin",
          "silverCoin","goldCoin", "goldCoin", "goldCoin", "ruby", "ruby" ]

def search():
    print("search...")
    found = random.choice(rarity)
    room = i.diver["bag"]["capacity"] - len(i.diver["bag"]["inventory"])
    while True:
        print(f"You found a {items[found]['description']}.")
        print(f"You have {room} spots left in your bag. "
              + "What do you want to do? ")
        print(f" - Keep the {items[found]['name']} (keep)")
        print(f" - Leave the {items[found]['name']} (leave)")
        choice = input("Choice: ").lower()
        if choice == "keep":
            keep(found)
            break
        elif choice == "leave":
            leave(found)
            break
        else:
            print("not an option...try again")


def add_to_inventory(item):
    i.diver["bag"]["inventory"].append(item)


def keep(item):
    print("keep...")
    add_to_inventory(item)
    i.consume_air()

def leave(item):
    print(f"leave {items[item]['name']}...")
    i.consume_air()


