import time, os

class Player:

    wiz_club = True

    def __init__(self, name="anonym", age=0):
        if age >= 18:
            self.name = name
            self.age = age
        
    def a(self):
        return "Utok"

    def age_checker(self):
        if self.age < 18:
            print("Jdi dopici")

class Head(Player):

    def __init__(self, type, name, age):
        super().__init__(name, age)
        self.type = type
    def a(self):
        return "Uutok"

# p1 = Player("Name", 18)
# print(p1.a())
# print(p1.age)
# print(p1.attack())
# print("----------------------------------------------------------------------------------------------------------------------------------------")
# # time.sleep(1.5)
# # os.system("cls")

p2 = Head("good", "Lojza", 77)

# print(p2.name)
# print(p2.type)
# print(p2.age)
# print(p2.a())
# print(p2.a())
