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

# print(players)

max_score = 50
player_scores = [0 for _ in range(players)] # pour chaque joueur, on place un "0" dans la liste des scores / range permet de boucler

# print(player_scores)

while max(player_scores) < max_score:

    current_score = 0 # initialisation de la variable

    for player_index in range(players):
        print("\nPlayer number", player_index + 1, "turn has started!\n") # \n ajoute un saut à la ligne
        print("Your total score is:", player_scores[player_index], "\n") # j'affiche je score du joueur avant la partie
        while True:
            should_roll = input("Would you like to roll (y)?")
            if should_roll.lower() != "y": # on parse 
                break

            value = roll()
            if value == 1:
                current_score = 0
                print("You rolled a 1! Turn done!")
            else:
                current_score += value # incrémente
                print("You rolled a: ", value)

            print("Your score is:", current_score)

        player_scores[player_index] += current_score # j'incremente le score du joueur
        print("Your total score is:", player_scores[player_index]) # j'affiche le score du joueur

max_score = max(player_scores)
winning_index = player_scores.index(max_score)
print("Player", winning_index + 1, "is the winner with the score of:", max_score)


