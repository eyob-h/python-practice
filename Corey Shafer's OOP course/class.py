import datetime
class Employee:
    # num_of_employees_self = 0
    num_of_employees = 0
    raise_amount = 1.04
    def __init__ (meself,fname,lname,pay):
        meself.fname = fname
        meself.lname = lname
        meself.pay = pay
        Employee.num_of_employees += 1 #returns the true num which is 2
        # meself.num_of_employees_self += 1  #returns 0


    def full_name(meself):
        return ('full name: {} {}'.format(meself.fname, meself.lname))
    

    #using classmethod as alternative constructor
    @classmethod
    def from_string(cls, emp_info):
        fname, lname, pay = emp_info.split("-")
        return cls(fname,lname,pay)
    
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @staticmethod
    def is_weekday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


    @property
    def email(meself):
        return ('{}.{}@gmail.com'.format(meself.fname, meself.lname))
    
    def apply_raise(meself):
        meself.pay = int(meself.pay*meself.raise_amount)


r = Employee("russ","wb",90000)
r.full_name()

mj = Employee("michael", "j", 10000)
mj.full_name()

print(r.email)


print(Employee.num_of_employees)
# print(Employee.num_of_employees_self)

rus = Employee.from_string("russel-westbrook-1000000")
print(rus.full_name())

my_date = datetime.date(2023, 3, 9)

print(Employee.is_weekday(my_date))




