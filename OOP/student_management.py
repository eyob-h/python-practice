class Student:
    def __init__ (self, name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

    def getGrade(self):
        return self.grade
    

class Course:
    def __init__(self,name, max_students, ):
        self.name = name
        self.max = max_students
        self.students = []

    def addStudent(self, student):
        if(len(self.students)< self.max):
            self.students.append(student)
        else:
            print("Max no of students reached")

    def getAverage(self):
        tot = 0
        for i in self.students:
            tot += i.getGrade()
            av = tot/len(self.students)
        
        print("The average grade is: ", round(av,2))
    
    def getTotEnrolled(self):
        # return len(self.students)
        print("The total students enrolled: ", len(self.students))


bob = Student("bob", 20, 89)
m = Student("mike", 21, 90)
r = Student("russ", 22, 99)
# print(bob.getGrade())
math = Course("Math",3)
# print(math.students[0].name)
math.addStudent(bob)
math.addStudent(r)
math.addStudent(m)

math.getAverage()
math.getTotEnrolled()


