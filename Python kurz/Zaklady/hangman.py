import random
import math
from Zaklady.hangman_pic import stages

words = ["harry", "ronald", "albus", "hermiona", "draco", "ron"]
rand_word = words[random.randint(0, len(words) - 1)]
#print(rand_word)
hidden = []
for i in range(0, len(rand_word)):
    hidden.append("_")

for i in range(0, len(rand_word)):
    print(hidden[i],end="")
print()

lives = 6
print(stages[lives])
while "_" in hidden:
    guess = input("zadejte hadane pismeno: ").lower()    

    for i in range(0, len(rand_word)):
        if guess == rand_word[i]:
            hidden[i] = guess

    if guess not in rand_word:
        lives -= 1
        print(stages[lives])
    print(f"Pocet zivotu {lives}.")
    if lives == 0:
        print("Prohra")
        break

    for i in range(0, len(rand_word)): 
         print(hidden[i],end="")
    print()


    if "_" not in hidden:
        print("Vyhrali jste!!")