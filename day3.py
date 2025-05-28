#Step1 : While loops

# The 'while' loop repeatedly executes a block of code as long as a given condition is True.
# It is useful when the number of iterations is not known in advance.

print("Are you sure you want to continue? (continue/cancel)")
while True:  # This creates an infinite loop that will only stop with a 'break' statement.
    choice = input("Please input your desicion: ").lower().strip()
    # The loop asks the user for input, converts it to lowercase, and removes extra spaces.
    if choice == "continue":
        print("All the Best!")
        break  # 'break' exits the loop immediately.
    elif choice == "cancel":
        print("Right Desicion!")
        break  # 'break' exits the loop immediately.
    else:
        print("Please input a valid choice: continue or cancel")
        continue  # 'continue' skips the rest of the loop and starts the next iteration.

# Note: Be careful with 'while True' loops. Always ensure there is a way to exit the loop (like 'break').


#Step2 : For loops
# The 'for' loop iterates over a sequence (like a list, tuple, or string) and executes a block of code for each item in the sequence.
# It is useful when the number of iterations is known in advance eg:, ideal for processing game elements like inventory items or rooms.

#example 1: To iterate through a list of items in a game armory.
print("Your armory has the following list of items.")
items = ["sword", "shield", "potion", "bow", "arrow"]
for item in items:
    print(f"- {item}.")  # This prints each item in the list. 

#example 2: To iterate through a range of numbers, which is useful for counting or repeating actions.
print("Counting up from 1 to 5:")
for int in range(1, 6):  # range(1, 6) generates numbers from 1 to 5.
    print(int)  # This prints each number in the range.

print("Counting down from 5 to 1:")
for int in range(5, 0, -1):  # range(5, 0, -1) generates numbers from 5 to 1.
    print(int)  # This prints each number in the range.

print("Counting up from 1 to 10 with a step of 2:")
for int in range(1, 11, 2):  # range(1, 11, 2) generates numbers from 1 to 10 with a step of 2.
    print(int)  # This prints each number in the range.

print("Counting down from 10 to 1 with a step of 2:")
for int in range(10, 0, -2):  # range(10, 0, -2) generates numbers from 10 to 1 with a step of 2.
    print(int)  # This prints each number in the range.

#example 3: To iterate through a string, which is useful for processing characters in a word or sentence.
print("Iterating through the word 'adventure':")
word = "adventure"
for char in word:
    print(char)  # This prints each character in the word 'adventure'.

#example 4: To iterate through a dictionary, which is useful for processing key-value pairs in game data.
print("Your character's stats:")
character_stats = {
    "health": 100,
    "strength": 75,
    "agility": 50,
    "intelligence": 60
}
for stat, value in character_stats.items():
    print(f"{stat.capitalize()}: {value}")  # This prints each stat and its value in the character's stats dictionary.

#example 5: To iterate through a set, which is useful for processing unique items in a game inventory.
print("Your unique items in the inventory:")
unique_items = ["sword", "shield", "potion", "bow", "arrow", "potion", "sword"]  # Note: 'potion' and 'sword' are duplicates.
for item in set(unique_items):  # Using 'set' to ensure unique items are processed,avoiding duplicates.
    # This converts the list to a set to remove duplicates and then iterates through it.    
    print(f"- {item}.")  # This prints each unique item in the inventory.
# Note: 'for' loops are generally preferred over 'while' loops when the number of iterations is known or when iterating over a sequence.

#Step3 : Nested loops
# Nested loops are loops inside another loop. They are useful for iterating through multi-dimensional data structures, like grids or matrices.
#example 1: To iterate through a 2D grid, which is useful for processing game maps or levels.
print("Iterating through a 2D grid:")
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in grid:  # Outer loop iterates through each row in the grid.
    for cell in row:  # Inner loop iterates through each cell in the current row.
        print(cell, end=" ")  # This prints each cell in the row, separated by a space.
    print()  # This prints a newline after each row for better readability. 

#example 2: To iterate through a list of lists, which is useful for processing game inventories or character stats.
print("Iterating through a list of lists:")
inventory = [
    ["sword", "shield", "potion"],
    ["bow", "arrow", "quiver"],
    ["armor", "helmet", "boots"]
]
for category in inventory:  # Outer loop iterates through each category in the inventory.
    print("Category:")
    for item in category:  # Inner loop iterates through each item in the current category.
        print(f"- {item}.")  # This prints each item in the category.
    print()  # This prints a newline after each category for better readability.

#example 3: To iterate through a dictionary of lists, which is useful for processing game data with multiple attributes.
print("Iterating through a dictionary of lists:")  
game_data = {
    "characters": ["hero", "villain", "sidekick"],
    "locations": ["forest", "castle", "village"],
    "items": ["sword", "shield", "potion"]
}
for key, values in game_data.items():  # Outer loop iterates through each key-value pair in the dictionary.
    print(f"{key.capitalize()}:")  # This prints the key (category) in the dictionary.
    for value in values:  # Inner loop iterates through each value in the current key's list.
        print(f"- {value}.")  # This prints each value in the list.
    print()  # This prints a newline after each category for better readability.  
# Note: Nested loops can lead to increased complexity and performance issues, especially with large datasets.
# Always consider the efficiency of your loops and try to minimize nesting when possible.


#Step4 : Loop control statements
# Loop control statements allow you to modify the behavior of loops, such as skipping iterations or exiting loops early.
#example 1: Using 'break' to exit a loop early.
# This is useful when you want to stop processing once a certain condition is met.
# For example, if you want to stop searching for an item in a game inventory once you find it.

print("Searching for an item in the inventory:")
inventory = ["sword", "shield", "potion", "bow", "arrow"]
item_to_find = "potion"
for item in inventory:
    if item == item_to_find:
        print(f"Found the item: {item}.")  # This prints the item once it is found.
        break  # 'break' exits the loop immediately after finding the item.
print("Finished searching the inventory.")

#example 2: Using 'continue' to skip an iteration.
# This is useful when you want to skip processing certain items in a loop.

print("Processing items in the inventory, skipping potions:")
for item in inventory:
    if item == "potion":
        print("Skipping potion.")  # This prints a message when skipping the potion.
        continue  # 'continue' skips the rest of the loop and starts the next iteration.
    print(f"Processing item: {item}.")  # This prints each item that is not a potion.


#example 3: Using 'pass' to do nothing in a loop.
# This is useful when you want to create a placeholder for future code without executing anything.
print("Processing items in the inventory, doing nothing for potions:")
for item in inventory:
    if item == "potion":
        pass  # 'pass' does nothing, allowing the loop to continue without any action.
    else:
        print(f"Processing item: {item}.")  # This prints each item that is not a potion.


#example 4: Using 'else' with loops.
# The 'else' block after a loop executes when the loop completes normally (not interrupted by 'break').
print("Processing items in the inventory with an else block:")
for item in inventory:
    if item == "potion":
        print("Found a potion, processing it.")  # This prints a message when a potion is found.
        break  # 'break' exits the loop immediately after finding the potion.
else:
    print("No potions found in the inventory.")
# The 'else' block will not execute if the loop is exited with 'break'.


#example 5: Using 'for-else' with a search operation.
print("Searching for an item in the inventory with an else block:")
item_to_find = "axe"  # Item that is not in the inventory.
for item in inventory:
    if item == item_to_find:
        print(f"Found the item: {item}.")  # This prints the item if found.
        break  # 'break' exits the loop immediately after finding the item.
else:
    print(f"{item_to_find} not found in the inventory.")
# The 'else' block will execute if the item is not found, indicating that the search was unsuccessful.
# Note: Loop control statements are powerful tools for managing the flow of loops and can help improve code readability and efficiency.
# Always use them judiciously to avoid confusion and maintain code clarity.


#Hands-on Exercise
print("Take action(fight/rest/flee):")
while True:  # This creates an infinite loop that will only stop with a 'break' statement.
    action = input("Please input your action: ").lower().strip()
    # The loop asks the user for input, converts it to lowercase, and removes extra spaces.
    if action == "fight":
        print("You chose to fight! Prepare for battle!")
        break
    elif action == "rest":
        print("You chose to rest! Regain your strength!")
        break
    elif action == "flee":
        print("You chose to flee! Escape safely!")
        break
    else:
        print("Invalid action! Please choose fight, rest, or flee.")
        continue



# Adventure loop with choices
player_name = input("Enter your character’s name: ").strip()
health = 100
print(f"\nWelcome, {player_name}, to the adventure!")

while health > 0:
    action = input("Choose an action (explore/rest/quit): ").lower()
    if action == "explore":
        damage = 20
        health = health - damage
        print(f"{player_name} explores and takes {damage} damage.")
    elif action == "rest":
        healing = 15
        health = health + healing
        print(f"{player_name} rests, recovering {healing} health.")
    elif action == "quit":
        print(f"{player_name.upper()} ends the adventure!")
        break
    else:
        print("Invalid action. Choose 'explore', 'rest', or 'quit'.")
    
    # Display health status
    print(f"Health: {health}")
    if health <= 0:
        print("Game Over! You’ve been defeated.")
        break
# Note: This code demonstrates the use of loops, conditionals, and user input to create a simple text-based adventure game.
# The player can explore, rest, or quit the game, with health management included.