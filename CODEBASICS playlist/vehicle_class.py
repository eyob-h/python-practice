class Vehicle:
    def __init__ (self, type):
        self.type = type
    
    def show_general_usage(self):
        print(f"General usage of {self.type} is transportation!")


class Car(Vehicle):
    def __init__ (self, model):
        self.type = "car"
        self.model = model
    
    def show_specific_usage(self):
        print("for going to work")

class Motor(Vehicle):
    def __init__ (self, model):
        self.type = "motor"
        # super().__init__(type)
        # super().type = self.type
        # super().type = type
        self.model = model
    
    def show_specific_usage(self):
        print("for racing")


boxer = Motor("Boxer")
# print(boxer)
boxer.show_general_usage()
boxer.show_specific_usage()

toyota = Car("Toyota")
toyota.show_specific_usage()
toyota.show_general_usage()