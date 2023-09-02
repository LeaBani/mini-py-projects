import random

# je créé une variable value qui stocke un nombr aléatoire
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

value = roll()

print(value)