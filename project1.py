import random

# je créé une variable value qui stocke un nombr aléatoire
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

# value = roll()

# selection du nombre de joueurs
while True:
    players = input("Enter the number of players (2-4):")
    if players.isdigit(): # je vérifie le type
        players = int(players) # je parse
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players")

    else:
        print("Invalid try again")
print(players)