class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
dog_1 = Dog("Pes", 5)
dog_2 = Dog("Pess", 8)
dog_3 = Dog("Pesss", 4)


def oldest(*args):
   return max(args)
result = oldest(dog_1.age, dog_2.age, dog_3.age)
print(result)