class Employee:
    num_of_employees = 0
    raise_amount = 1.04
    def __init__ (meself,fname,lname,pay):
        meself.fname = fname
        meself.lname = lname
        meself.pay = pay
        Employee.num_of_employees += 1

    def full_name(meself):
        return ('full name: {} {}'.format(meself.fname, meself.lname))

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    
    def apply_raise(meself):
        meself.pay = int(meself.pay*meself.raise_amount)

#chain of order is called method resolution order
class Developer(Employee):
    def __init__ (self, fname, lname, pay, lang):
        super().__init__(fname,lname,pay)
        self.lang = lang

class Manager(Employee):
    def __init__(self, fname, lname, pay, employees=None):
        super().__init__(fname,lname,pay)
        if employees == None: 
            self.employees = []
        else:
            self.employees = employees
            
    def add_employee(self, empl):
        if empl not in self.employees:
            self.employees.append(empl)
    
    def remove_employee(self, empl):
        if empl in self.employees:
            self.employees.remove(empl)

    def show_employees(self):
        for emp in self.employees:
            print(emp.full_name())
kob = Developer('kob','bean',10000000,'python')
manu = Developer('manu','kd',10000000,'c++')

m = Manager('steve','curr',900000)
m.add_employee([manu])
m.add_employee([kob])

m.show_employees()
# m.add_employee('kd')
# m.add_employee('dg')


# m.remove_employee('dg')
# print(m.employees)
# print(help(Developer))
