#Step 1: Arithmetic Operations

character_health = 5
attack = 1*2
healing = 1

character_health = character_health - attack
print("Your current lives is:", character_health)

character_health = character_health + healing
print("Reedemed lives update now is:",character_health)

survival = character_health // attack
print("You can only survive after",survival,"attacks☠️.")



#Step 2: UserInputs
username = input("Enter your username:")
age = int(input("Enter your age:"))
lives = 5
damage = 1*1

print("\n==================================\n")
print("Welcome", username ,"@", age , "to Lord's Mobile☠️.")
print("\n==================================")
print("Your initial lives is:",lives)

lives = lives - damage
print("You received an attack,your current lives is:",lives)

survival = lives // damage
print("You can only survive a max of",survival, "attacks.")

#Step3 : Conditionals
if lives < 2 :
    print("You are running out of lives❤️!")
elif lives < 4 :
    print("Steady but dangerous☠️")
else:
    print("Healthy👍")    




#Final Exercise
player_name = input("Enter your character’s name: ")
health = int(input("Enter your starting health (e.g., 100): "))
print("\nA wild beast appears!")
action = input("Choose an action (attack/heal): ").lower()
# Process choice
if action == "attack":
    damage_dealt = 20
    damage_taken = 15
    health = health - damage_taken
    print(player_name, "attacks, dealing", damage_dealt, "damage!")
    print("The beast hits back for", damage_taken, "damage.")
elif action == "heal":
    healing = 25
    health = health + healing
    print(player_name, "uses a potion, restoring", healing, "health!")
else:
    print("Invalid choice! You hesitate, and the beast attacks!")
    health = health - 10

# Display health
print("Current health:", health)

# Health status
if health <= 0:
    print("Game Over! You’ve been defeated.")
elif health > 75:
    print("You’re ready for the next challenge!")
else:
    print("You’re weakened—choose wisely next time!")