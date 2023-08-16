from data import MENU
from data import resources
import os


def ingred(typ):
    resources["water"] -= MENU[typ]["ingredients"]["water"]
    resources["milk"] -= MENU[typ]["ingredients"]["milk"]
    resources["coffee"] -= MENU[typ]["ingredients"]["coffee"]
    if resources["water"] >= 0 and resources["milk"] >= 0 and resources["coffee"] >= 0:
        print("Na vas napoj mame dostatek ingredienci.")
        a = 1
        return a
    else:
        print("Nemame dostatek ingredienci na tento napoj.")
        a = 0
        return a
    
def mm(money):
    print("Prosim vlozte mince 1, 2, 5, 10, 20, 50")
    money += int(input("Kolik 1 Kc chcete vlozit?: "))
    money += 2 * int(input("Kolik 2 Kc chcete vlozit?: "))
    money += 5 * int(input("Kolik 5 Kc chcete vlozit?: "))
    money += 10 * int(input("Kolik 10 Kc chcete vlozit?: "))
    money += 20 * int(input("Kolik 20 Kc chcete vlozit?: "))
    money += 50 * int(input("Kolik 50 Kc chcete vlozit?: "))

    print(f"Celkem jste vlozili: {money} Kc.")

    if money > MENU[type_of_cof]["cost"]:
        back = money - MENU[type_of_cof]["cost"]
        print(f"Vratili jsme vam: {back} Kc")
        print("Napoj se pripravuje.")
    elif money < MENU[type_of_cof]["cost"]:
        print(f"Vhodili jste nedostatek penez.")
        mm(money)
    else:
        print("Napoj se pripravuje.")
         
while True:
    type_of_cof = input("Co by jste si dal? (espresso/latte/cappuccino): ").lower()
    if type_of_cof == "report":
        print(f"Voda: {resources['water']}\nMleko: {resources['milk']}\nKava: {resources['coffee']}")
    else:    
        print(f"Cena {type_of_cof} je {MENU[type_of_cof]['cost']}Kc.")
        a = ingred(type_of_cof)
        if a == 0:
            break
        print(resources)
        money = 0
        mm(money)