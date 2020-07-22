#Python Object-Oriented Programming


class Employee:

    numofemps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first +'.'  + last + '@company.com'
        Employee.numofemps += 1

    def fullname(self):
        return self.first +' '+ self.last
    
    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self,other):
        return self.pay + other.pay

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else :
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
        
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev1 = Developer('Ronit', 'Shukla', 90000, 'Python')
dev2 = Developer('Shivani', 'Shukla', 125000, 'Java')

mgr1 = Manager('Ulrich', ' Nielsen', 3000000, [dev1])

# print(dev1)

print(dev1+dev2)

# print(repr(dev1))
# print(str(dev1))

# print(dev1.pay)
# dev1.apply_raise()
# print(dev1.pay)


# print(emp1.email)
# print(emp2.email)
