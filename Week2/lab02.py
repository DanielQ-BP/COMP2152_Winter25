import random

# Array of weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

# Rolls a die between 1 and 6
def roll_dice():
    return random.randint(1, 6)

# Simulates the weapon roll
try:
    weaponRoll = roll_dice()
    print(f"You rolled a {weaponRoll}.")

    # Add the weaponRoll to hero's combat strength (assuming combat strength is initially 0)
    combat_strength = 0 + weaponRoll
    print(f"Your combat strength is now {combat_strength}.")

    # Use the weaponRoll as an index to pick the weapon
    weapon = weapons[weaponRoll - 1]  # weaponRoll is between 1 and 6, so subtract 1 to use it as an index
    print(f"Your weapon is: {weapon}")

    if weaponRoll <= 2:
        print("You rolled a weak weapon, friend.")
    elif weaponRoll <= 4:
        print("Your weapon is meh.")
    else:
        print("Nice weapon, friend!")

    # Checks if the weapon rolled is not a Fist
    if weapon != "Fist":
        print("Thank goodness you didn't roll the Fist...")

except ValueError:
    print("Error: Invalid input. Please ensure the input is an integer.")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")
    exit()
