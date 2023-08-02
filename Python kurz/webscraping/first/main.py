#
# with open("names.txt") as names:
#     l_names = names.readlines()
#     for i in l_names:
#         i = i.strip()
#         with open(f"output/guest_{i}.txt", mode="w") as g:
#             g.write("Ahoj")

# con = "ano"
# while con == "ano":
#     title = input("Zadejte nazev souboru: ")
#     with open(f"output/{title}.txt", mode="w"):
#         print("Soubor byl uspesne vytvoren")
#         con = input("ano/ne\n").lower()

try:
    with open("chyba.txt", mode="w") as x:
        print(x.read())
except FileNotFoundError as nn:
    print("Soubor nenalezen")
except IOError as inout:
    print("IO chyba")
