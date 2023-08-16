
print("Vitejte na horske draze")

height = int(input("Zadej vysku v cm:\n"))
bill = 0

if height >= 87:
    print("Muzete jet :-)")
    age = int(input("Kolik ti je let?\n"))

    if age < 12:
        bill += 50
        print("Cena listku je 50 Kc") 
    elif 12 <= age < 18:
        bill += 100
        print("Cena listku je 100 Kc")
    elif 40 <= age <= 50:
        bill += 0
        print("Zdarma.")
    else:
        bill += 150
        print("Cena listku je 150 Kc")
    photo = input("Chcete fotku??\n")

    if photo == "ano" or "Ano":
        bill += 40
    print(f"Vase cena je {bill} Kc.")

else:
    print("Nemuzete jet :-(")
