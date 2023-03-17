class Pet:
    howManySpecies = 0

    def __init__ (self,name):
        self.name = name
        Pet.incrementPetCount()

    def show(self):
        greet = (f"I am {self.name}")
        print(greet)
        # print(Pet.sayThankyou(greet))

    def speak(self):

        print(f"Hi")

    @classmethod
    def numberOfSpecies(cls):
        return(cls.howManySpecies)
    
    @classmethod
    def incrementPetCount(cls):
        cls.howManySpecies +=1

    @staticmethod
    def sayThankyou(string):
        return string + " Thank you :)"


class Cat(Pet):
    def __init__ (self,name,color):
        super().__init__(name)
        self.color = color
    def speak(self):
        print("Meow")

    def show(self):
        greets = (f"I am {self.name}, and I'm {self.color}")
        print(super().sayThankyou(greets))

class Dog(Pet):
    def speak(self):
        print("Bark")


wero = Cat("The wero", "Green")
wero.show()
wero.speak()

bobby = Dog("Bob")
bobby.show()
bobby.speak()

fish = Pet("Varush")
fish.show()
fish.speak()

print(f"Number of pets = {Pet.numberOfSpecies()}")