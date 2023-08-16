from Zaklady.auctionlogo import auction_logo
import os


print("Vitejte v programu pro tichou drazbu.")
print(auction_logo)

def winner(dia):
    max = 0
    max_name = ""
    for i in dia:
        if dia[i] > max:
            max = dia[i]
            max_name = i
    print(f"Vitezem je {max_name} s nabidkou {max}$.")


bidders = {}
condition = "ano"
while condition == "ano":
    name = input("Jake je vase jmeno? ")
    bid = int(input("Jaka je vase nabidka? "))

    bidders[name] = bid

    condition = input("Jsou dalsi nabizejici (ano/ne)? ")
    if condition == "ne":
        os.system("cls")
    print()
winner(bidders)