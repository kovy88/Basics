import random
import os
from Zaklady.pic import logo

print(logo)

print("Vitejte ve hre Guess the number\nMyslim si cislo od 1 do 100")
repeat = "yes"

while repeat == 'yes':
    diff = input("Vyberte obtiznost. hard / easy: ").lower()

    lives = 0
    guess = random.randint(1, 100)

    if diff == "easy":
        lives = 10
    elif diff == "hard":
        lives = 5

    while lives > 0:
        print(f"Vas pocet zbyvajicich pokus je {lives}.")
        num = int(input("Tipnete si cislo: "))
        if num == guess:
            print(f"Vyborne vyhrali jste. Hadane cislo bylo {guess}.")
            break
        elif num < guess:
            lives -= 1
            print("Hadane cislo je vetsi.")
        else: 
            lives -= 1
            print("Hadane cislo je mensi.")

        if lives == 0:
            print(f"Prohrali jste. Hadane cislo bylo {guess}.")

    repeat = input("Chcete pokracovat? yes/no\n")
    os.system("cls")
    