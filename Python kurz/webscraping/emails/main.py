with open("In/general.txt") as letter:
    letter = letter.read()

with open("In/Namex.txt") as names:
    nms = names.readlines()
    for i in nms:
        i = i.strip()
        fin = letter.replace("[name]", i)
        with open(f"Out/guest_{i}.txt", mode="w") as nevim:
            nevim.write(fin)
