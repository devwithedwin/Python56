"""
Step 1: Lists

A list is an ordered, mutable collection of items (e.g., strings, numbers) stored in square brackets []. Lists are perfect for game elements like an inventory or a list of enemies.
Key List Operations

    Create: items = ["sword", "potion"]
    Access: items[0] → "sword" (0-based indexing).
    Modify: items[0] = "axe" changes the first item.
    Add: items.append("shield") adds to the end.
    Remove: items.remove("potion") removes by value; items.pop(1) removes by index.
    Length: len(items) returns the number of items.
    Loop: Use for item in items to iterate (from Day 3).

"""

print("My stationery:")
stationery = ["Pen","Pencil","Eraser","Sharpener","Notebook"]
print(stationery)

stationery.append("Ruler")
print("After adding Ruler:")
print(stationery)

stationery.extend(["Celltape", "Crayons"])
print("After extending with Celltape and Tape:")
print(stationery)


#backup the current stationery list before clearing it
backup = stationery.copy()

stationery.clear()
print("After clearing the list:")
print(stationery)

stationery = backup
print("After restoring the list:")
print(stationery)

stationery.remove("Pen")
print("After removing Pen:")
print(stationery)

# Replace the first item (Pencil) with Marker
stationery[0] = "Marker"
print("After replacing Pencil with Marker:")    
print(stationery)

print("Length of stationery list:", len(stationery))
print(len(stationery))

# Check if "Pen" is in the stationery list
if "Pen" in stationery:
    print("Pen is in the stationery list.") 
else:
    print("Pen is not in the stationery list.")

# sort the stationery list in alphabetical order
stationery.sort()
print("After sorting the stationery list:")
print(stationery)

stationery.reverse()
print("After reversing the stationery list:")
print(stationery)

stationery.insert(2, "Highlighter")
print("After inserting Highlighter at index 2:")    
print(stationery)

print(len(stationery))

"""
Step 2: Dictionaries

A dictionary stores key-value pairs in curly braces {}, ideal for structured game data like player stats (e.g., health: 100, name: "Elara").
Key Dictionary Operations

    Create: player = {"name": "Elara", "health": 100}
    Access: player["health"] → 100.
    Modify: player["health"] = 80 updates the value.
    Add: player["gold"] = 50 adds a new key-value pair.
    Remove: del player["gold"] removes a key-value pair.
    Loop: for key, value in player.items(): iterates over pairs.
    Check Key: "name" in player returns True if the key exists.

"""

player = {
    "name": "Elara",
    "health": 100,
    "gold": 50,
    "level": 1
}
print("Player Info:")
print(player)

# Accessing player information
print("Player Name:", player["name"])
print(f"Player Name:{player['name']}")

# Modifying player health
player["health"] = 80
print("Player Health after damage:", player["health"])

# Adding a new key-value pair for experience
player["experience"] = 200
print("Player Info after adding experience:")
print(player)

# Removing the gold key-value pair
del player["gold"]
print("Player Info after removing gold:")
print(player)

# Looping through player information
for key, value in player.items():
    print(f"{key}: {value}")

# Checking if a key exists
if "level" in player:
    print("Player has a level key.")
else:
    print("Player does not have a level key.")

# Checking if a key does not exist
if "mana" not in player:
    print("Player does not have a mana key.")
else:
    print("Player has a mana key.")


#Hands-on Exercise:
# Battle with inventory
player = {
    "name": input("Enter your character’s name: ").strip(),
    "health": 100,
    "inventory": ["sword", "potion", "shield"]
}
enemies = ["goblin", "troll"]

print(f"\n{player['name']}, prepare for battle!")
for enemy in enemies:
    print(f"\nA {enemy.upper()} attacks!")
    action = input("Use an item (sword/potion/shield/none): ").lower()
    
    if action in player["inventory"]:
        if action == "sword":
            print(f"{player['name']} attacks with {action}, dealing 20 damage!")
        elif action == "potion":
            player["health"] += 15
            player["inventory"].remove(action)
            print(f"Used {action}, health restored to {player['health']}.")
        elif action == "shield":
            print(f"{action.capitalize()} blocks 10 damage!")
    else:
        print(f"No {action} in inventory! Took 15 damage.")
        player["health"] -= 15
    
    print(f"Health: {player['health']}")
    if player["health"] <= 0:
        print("Game Over!")
        break
else:
    print(f"{player['name']} defeated all enemies!")


#Hands-on Exercise:
# Game inventory manager
player = {
    "name": input("Enter your character’s name: ").strip(),
    "health": 100,
    "inventory": ["sword", "potion"]
}

print(f"\nWelcome, {player['name']}!")
while True:
    print("\nCurrent inventory:", player["inventory"])
    print(f"Health: {player['health']}")
    action = input("Choose action (add/remove/damage/quit): ").lower()
    
    if action == "add":
        item = input("Enter item to add: ").strip()
        player["inventory"].append(item)
        print(f"Added {item} to inventory.")
    elif action == "remove":
        item = input("Enter item to remove: ").strip()
        if item in player["inventory"]:
            player["inventory"].remove(item)
            print(f"Removed {item} from inventory.")
        else:
            print(f"{item} not in inventory!")
    elif action == "damage":
        damage = int(input("Enter damage taken: "))
        player["health"] -= damage
        print(f"Took {damage} damage. Health: {player['health']}")
        if player["health"] <= 0:
            print("Game Over! You’ve been defeated.")
            break
    elif action == "quit":
        print(f"{player['name'].upper()} ends the adventure!")
        break
    else:
        print("Invalid action. Choose 'add', 'remove', 'damage', or 'quit'.")    








