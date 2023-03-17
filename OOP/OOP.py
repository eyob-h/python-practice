class Dog:

    def __init__ (self, n, a):
        self.name = n
        self.age = a

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def setName(self,x):
        self.name = x

    def setAge(self,x):
        self.age = x

    # def bark(self):
    #     print("bark")


bobby = Dog("bob",30)
y=bobby.getAge()
print(y)
bobby.setAge(45)
print(bobby.getAge())

bobby.setName("mark")
print(bobby.getName())
bobby.setAge(100)
print()