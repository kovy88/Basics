from Zaklady.dat_hi_low import data
import random
import os

def random_num(num):
    lenght = len(data)
    num = random.randint(0, lenght - 1) 
    return num

ran_num1 = 0
ran_num2 = 0
ran_num1 = random_num(ran_num1) 
ran_num2 = random_num(ran_num2)
score = 0

while True:
    ran_num1 = ran_num2
    ran_num2 = random_num(ran_num2)
    if ran_num1 == ran_num2:
        ran_num2 = random_num(ran_num2)

    print(f"Porovnejte A: {data[ran_num1]['name']}, {data[ran_num1]['description']}, z {data[ran_num1]['country']}")
    print(f"Porovnejte B: {data[ran_num2]['name']}, {data[ran_num2]['description']}, z {data[ran_num2]['country']}")

    fol1 = data[ran_num1]['follower_count']
    fol2 = data[ran_num2]['follower_count']

    print(f"Test {fol1}")
    print(f"Test {fol2}")

    answer = input("Kdo ma vice sledujicich? ")

    if (fol1 > fol2 and answer == 'A') or (fol2 > fol1 and answer == 'B'):
        score += 1
        print(f"Uhadli jste. Vase skore je {score}")

    else: 
        print(f"To je spatne. Vase skore je {score}")
        break
