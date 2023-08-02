import math
import random

#name = input("Jake je tve jmeno??\n")
#
#print("Ahoj jsem " + name + ".")
#
#
#age = 40
#age +=1
#print(age)
#
#city = input("Mesto kde bydlis??\n")
#print("Bydlim ve meste "+ city + ".")


#name = input("Tve jmeno??\n")
#length = len(name)
#print(name, length)




#print("Vitejte v aplikaci generovani jmen")
#name = input("Jake je tve kresstni jmeno?\n")
#character = input("Jaka je tva vlastnost?\n")
#print("Tvoje slozene jmeno je " + name + " " + character)



#age = 11
#print("Je mi " + str(age) + " let.")


#number = input("Napiste dvoumistne cislo:\n")
#result = int(number[0]) + int(number[1])
#print(result)


#height = input("Vyska v metrech:\n")
#weight = input("Vaha v kg:\n")
#bmi = int(weight) / float(height)**2 
#bmi = round(bmi, 2)
#print("Vas BMI je: " + str(bmi))

#x = 5 
#name = "David"
#print(f"{name} x ma hodnotu: {x}" )

#age = int(input("zadej vek:\n"))
#print(f"{90 - age} zbyva let, {(90 - age) * 12} mesicu, {(90 - age) * 52} tydnu, {(90 - age) * 365} dnu")


#print("Vitejte v kalkulatoru na vypocet plateb")
#price = int(input("Kolik mate zaplatit? "))
#bonus = int(input("Kolik date spropitneho  (v %)? "))
#people = int(input("Mezi kolik lidi se ma rozdelit castka? "))
#
#result = (price + price * (bonus / 100)) / people
#final = "{:.2f}".format(result)
#print(f"Kazdy clovek ma zaplatit {final} Kc")


#age = int(input("Zadejte svuj vek: "))
#
#if age >= 18:
#    print(":-)")
#else:
#    print(":-(")

#is_student = input("Jste student? ")
#if is_student == "ano" or is_student == "Ano":
#    print("Cena listku je 120Kc")
#else:
#    print("Cena listku je 150Kc")



#type = input("Jakt typ??\n")
#
#if type == "normal":
#    print(f"Cena telefonu {type} je 15Kc.")
#else:
#    print(f"Cena telefonu {type} je 25Kc.")


#weight = float(input("Zadejte vahu : "))
#height = float(input("Zadejte vysku (v metrech): "))
#
#bmi = weight / height**2
#bmi = round(bmi, 1)
#
#if bmi < 18.5:
#    print(f"Vase bmi je {bmi}. Mate podvahu.")
#elif 18.5 <= bmi < 25:
#    print(f"Vase bmi je {bmi}. :-)")
#elif 25 <= bmi < 30:
#    print(f"Vase bmi je {bmi}. Mate nadvahu.")
#elif 30 <= bmi < 35:
#    print(f"Vase bmi je {bmi}. :-(")
#else:
#    print(f"Vase bmi je {bmi}. Radsi nic. ")


#year = int(input("Zadej rok: "))
#
#if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#    print("Tento rok je prestuny.")
#else: 
#    print("Neni prestupny.")


#
#size = input("Jakou chcete velikost??\n")
#bill = 0
#if size == "S":
#    bill += 100
#elif size == "M":
#    bill += 150
#else:
#    bill += 200
#fefe = input("Chcete na ni feferonky??\n")
#
#if fefe == "ano" and size == "S":
#    bill += 20
#elif fefe == "ano":
#    bill += 30
#
#cheese = input("Chcete syr??\n")
#
#if cheese == "ano":
#    bill += 15
#print(f"Tady je vase pizza a stoji {bill} Kc.")



#import mymodule


#print(random.randint(1,6))

#print(random.random())

#print(random.randrange(15,25,3))

#print(math.ceil(5.1))
#print(math.floor(5.1))


#print(math.ceil(random.random() * 6))
#print(math.ceil(random.random() * 6))
#print(math.ceil(random.random() * 6))
#print(math.ceil(random.random() * 6))
#print(math.ceil(random.random() * 6))
#print(math.ceil(random.random() * 6))

#x = random.randint(0,1)
#if x == 0:
#    print("Panna")
#else:
#    print("Orel")



#employees = ["Jan", "Ron", "David"]
#
#
#employees.append("Harry")
#employees.extend(["Honza", "Pavel"])
#employees.remove("Ron")
#print(employees)


#names = input("Napis jmena vsech co sedi u stolu: ")
#people = names.split(" ")

#random_number = random.randint(0,len(people) - 1)

#print(f"{people[random_number]} si vytahl cernyho Petra a plati. :(")


#a = ["Jan", "Petr", "Pavel", "Lukas"]
#b = ["Anna", "Klara", "Nora", "Lenka"]
#
#students = [a, b]
#
#print(students[1][2])


#set1 = ["💩","💩","💩"]
#set2 = ["💩","💩","💩"]
#set3 = ["💩","💩","💩"]
#
#
#all_sets = [set1, set2, set3]
#
#print(f"{set1}\n{set2}\n{set3}")
#
#position = input("Zadejte souradnici: ")
#
#num1 = int(position[0])
#num2 = int(position[1])
#
#if num1 >= len(set1) or num2 >= 3:
#    print("Mimo vysec.")
#else:
#    all_sets[num1][num2] = "X"
#    print(f"{set1}\n{set2}\n{set3}")
#
#

#rock = '''
#    _______
#---'   ____)
#      (_____)
#      (_____)
#      (____)
#---.__(___)
#'''
# 
#paper = '''
#    _______
#---'   ____)____
#          ______)
#          _______)
#         _______)
#---.__________)
#'''
# 
#scissors = '''
#    _______
#---'   ____)____
#          ______)
#       __________)
#      (____)
#---.__(___)
#'''
#
#
#
#
#
#print("Hra kamen, nuzky, papir.")
#var = [rock, scissors, paper]
#user = int(input("Kamen / Nuzky / Papir  (0/1/2)\n"))
#print()
#print(f"Uzivatel si vybral: {var[user]}")
#print()
#pc = random.randint(0,2)
#
#print(f"Pocitac si vybral: {var[pc]}")
#print()
#
#if (user == 0 and pc == 1) or (user == 1 and pc == 2) or (user == 2 and pc == 0):
#    print("Vyhral si")
#elif user == pc:
#    print("Remiza")
#else:
#    print("Prohral si")
#

#ovoce = ["jablko", "hruska", "pomeranc"]
#
#for i in range(10):
#    print(i)
#

#heights = input("Vlozte vysku lidi\n")
#hei = heights.split(" ")
#sum = 0
#for i in hei:
#    sum += int(i)
#print(f"Prumerna vyska je {round(sum/len(hei), 2)}")



#score = input("Zadej skore: ")
#score_list = score.split(" ")
#sc_list = []
#
#for i in range(0, len(score_list)):
#    sc_list.append(int(score_list[i]))
#
#max = 0
#
#for i in sc_list:
#    if i > max:
#        max = i
#print(max)
#
#min = 10e10
#for i in sc_list:
#    if i < min:
#        min = i
#print(min)
#



#sum = 0
#
#for i in range(0, 101, 2):
#    sum += i
#print(sum)


#for i in range (1, 101):
#    if i % 3 == 0 and i % 5 == 0:
#        print("FizzBuzz")
#    elif i % 3 == 0:
#        print("Fizz")
#    elif i % 5 == 0:
#        print("Buzz")
#    else: print(i)
     
#letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#special_char = ['%', '#', '$', '!', '&', '(', ')', '*', '+', '?']
#
#num_of_let = int(input("Kolik pismen chcete mit ve svem heslu??\n"))
#num_of_num = int(input("Kolik cisel chcete mit ve svem heslu??\n"))
#num_of_cha = int(input("Kolik znaku chcete mit ve svem heslu??\n"))
#
#heslo = []
#for i in range(0, num_of_let):
#    x = random.randint(0,len(letters) - 1)
#    heslo += letters[x]
#for i in range(0, num_of_num):
#    x = random.randint(0,len(numbers) - 1)
#    heslo += numbers[x]
#for i in range(0, num_of_cha):
#    x = random.randint(0,len(special_char) - 1)
#    heslo += special_char[x]
#    
#translator = ""
#
#for i in range (0, 50):
#    random_num1 = random.randint(0, len(heslo) - 1)
#    random_num2 = random.randint(0, len(heslo) - 1)
#
#    translator = heslo[random_num2]
#    heslo[random_num2] = heslo[random_num1]
#    heslo[random_num1] = translator

#random.shuffle(heslo)
#
#result = ""
#
#for i in heslo:
#    result += i
#
#print(result)

#x = 0
#
#while x <= 10:
#    print(x)
#    x += 1

#characters = ["Harry", "Ron", "Hermiona", "Draco"]
#x = random.randint(0, len(characters) - 1)
#character = characters[x]
#guess = ""
#trys = 0
#while character != guess and trys < 2:
#    guess = input("Hadej postavu\n")
#    trys += 1
#if trys == 2:
#    print("Bohuzel")
#else: print("Vyborne")



#def my_fun():
#    print("Jmenuji se David")
#
#my_fun()

#def greet():
#    print("ahoj")
#    print("Jsem David")
#    print("ahoj")
#greet()

#def greet_name(name, age):
#    print(f"Ahoj ja jsem {name} a je mi {age}.")
#
#greet_name("David", 20)
#greet_name(age=18, name="Jan")


#height = int(input("Vyska zdi: "))
#width = int(input("Sirka zdi: "))
#coverage = 5
#
#def paint_calc(wheight, wwide, cover):
#     area = wheight * wwide 
#     number_of_cans = math.ceil(area / cover)
#     print(number_of_cans)
#
#paint_calc(height, width, coverage)

#def is_prime(number):
#    if number >= 4 and number != 5:
#        if number % 2 != 0:
#            if number % 3 != 0:
#                if number % 5 != 0:
#                    print("Toto je prvocislo.")
#                else:print("Neni")
#            else:print("Neni")
#        else:print("Neni")
#    else:print("Toto je prvocislo.")

#def is_prime(number):
#    res = "Je prvocislo"
#    for i in range(2, number):
#        if number % i == 0:
#            res = "Neni"
#            break
#    print(res)
#
#num = int(input("Zadejte cislo: "))
#
#is_prime(num)


#it_dict = {
#    "String":"Text",
#    "Int":"Cele cislo",
#    "Float":"Desetinne cislo"
#}
#print(it_dict)
#
#it_dict[4] = "Hmm"
#
#print(it_dict)
#
#it_dict[4] = "JSEm"
#
#print(it_dict)
 
#it_dict = {
#    "String":"Text",
#    "Int":"Cele cislo",
#    "Float":"Desetinne cislo",
#    "Boolean" :"Pravda Nepravda"
#}
#
#for key in it_dict:
#    print(it_dict[key])


#students_results = {
#    "Harry": 85,
#    "Ron": 71,
#    "Herminona": 98,
#    "Draco": 69,
#}

# Stupnice
# 91 až 100 = "Excelentní"
# 81 až 90 = "Vynikající"
# 71 až 80 = "Splněno"
# méně jak 71 = "Nesplněno"

#results = {}
#
#for key in students_results:
#    
#    score = students_results[key]
#    if 91 <= score <= 100:
#        results[key] = "Excelentni"
#    elif 81 <= score <= 90:
#        results[key] = "Vynikající"
#    elif 71 <= score <= 80:
#        results[key] = "Splněno"
#    else: results[key] = "Nesplněno"
#
#print(results)


#cities ={
#    "Spain":"Madrid",
#    "France":"Paris",
#    "England":"London"
#}#

#travel_diary = {
#    "Spain":["Madrid", "Leon", "Valencia"],
#    "France":["Paris", "Nice", "Rennes"],
#}
#
#print(travel_diary["France"][2])


#travel_diary = {
#    "Spain":{"visited_cities":["Madrid", "Leon", "Valencia"], "visits": 5},
#    "France":{"visited_cities":["Paris", "Nice", "Rennes"] , "visits": 3}
#}
#def aaaa(country, towns, visits, travel_diary):
#    travel_diary.append({"country":country,
#                        "visited_cities": towns,
#                        "visits": visits})
#
#state = input("Jaky stat chcete pridat?\n")
#town = input("Jaka mesta jste navstivil?\n")
#visit = int(input("Kolikrat jste v teto zemi byl?\n"))
#
#cities = town.split(" ")
#
#travel_diary = [
#    {
#        "country": "Spain",
#        "visited_cities": ["Madrid", "Leon", "Valencia"],
#        "visits": 5
#    },
#    {
#        "country": "France",
#        "visited_cities": ["Paris", "Nice", "Rennes"],
#        "visits": 2
#    }
#]
#print(travel_diary)
#aaaa(state, cities, visit,travel_diary)
#
#print(travel_diary)

#aa = {}
#
#aa["Matej"] = 500
#aa["KArel"] = 300
#aa["Arel"] = 1300
#
#print(aa)
#max = 0
#for i in aa:
#    if aa[i] > max:
#        max = aa[i]
#print(max)

#def sum(num1, num2):
#    print(num1 + num2)
#
#sum(5,5)



#def better_name(first_name, sec_name):
#    first_name = first_name.capitalize()
#    sec_name = sec_name.capitalize()
#    return f"{first_name} {sec_name}"
#better_name("jan", "zmrd")

#def better_name(first_name, sec_name):
#     fullname = first_name + " " + sec_name
##     return fullname.title()
##print(better_name("jan", "zmrd"))
#
#
#year = int(input("Zadej rok: "))
#month = int(input("Zadej mesic: "))
#
#res = ""
#if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#    res = "pres"
#else: 
#    res = "neni"
#
#days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#num_of_days = 0
#if res == "pres" and month == 1:
#    num_of_days = days_in_month[month - 1] + 1
#    print(num_of_days)
#else:  
#    num_of_days = days_in_month[month - 1]
#    print(num_of_days)




#def sum(num1, num2):
#    """Vrati soucet dvou cisel"""
#    return num1 + num2
#print(sum(5,3))


#
#def test():
#    global student
#    student = "Matej"
#    print(student)
#
#test()
#print(student)

#def test_function():
#  for number in range(1, 10):
#    if number == 10:
#      print("Vše je správně")
#test_function()


# Občas funguje a občas ne
#import random
#all_dice_numbers = ["1", "2", "3", "4", "5", "6"]
#dice_number = random.randint(0, 5)
#print(all_dice_numbers[dice_number])


## Mysli jako počítač
#year = int(input("Jaký je váš rok narození?"))
#if year > 1980 and year < 1994:
#  print("Jste millenial.")
#elif year >= 1994:
#  print("Jste generace Z.")


# Oprav hned chyby
#age = int(input("Kolik je vám let?"))
#if age > 18:
#    print(f"Ve věku {age} můžete kupovat alkohol.")


#def change(x_list):
#    res = []
#    for i in x_list:
#        i += 10
#        res.append(i)
#    print(res)
#change([1,2,3,4,5])

for number in range(1, 11):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print("number")