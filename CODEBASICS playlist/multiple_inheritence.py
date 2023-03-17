class Father:
    def skills(self):
        print("designing")

class Mother:
    def skills(self):
        print("programming")

class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("writing")

bob = Child()
bob.skills()
