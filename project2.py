# j'importe mon texte

with open("story.txt", "r") as f:
    # ici j'ouvre mon fichier txt, en mode "r" soit read / ou "w" write par exemple
    # with permets de créer un contexte dans lequel on éxécute notre programme (ici, dans f)
    story = f.read() # je stocke mon texte dans la var story
# print(story)

# je veux voir quels mots sont entourés de <>

# words = []
words = set() # permet de garder dans un set seules des valeurs uniques
start_of_word = -1 # trouver l'index du mot
target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i # si le caractère est égal à <, on update la variable à i

    if char == target_end and start_of_word != -1: # si la fin du mot est égal à > ET que le début du mot est différent de -1 (soit égale à i dans la condition précédente)
        word = story[start_of_word: i + 1] # "slice character": on commence avec start of words, on termine à i +1
        # words.append(word) # on ajoute le word à la liste
        words.add(word) # on ajoute le word au set avec "add"
        start_of_word = -1 # on reset la variable une fois que le mot à été trouvé

# print(words)

answers = {} # je créé un dictionnaire de correspondance clé/valeur

for word in words:
    answer = input("Enter a word for " + word + ": ") # concatenation d'une string et d'une var
    answers[word] = answer

    # print(answers)
for word in words:
    story = story.replace(word, answers[word])

    print(story)