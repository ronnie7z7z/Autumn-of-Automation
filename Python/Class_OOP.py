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

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount



emp1 = Employee('Ronit', 'Shukla', 90000)
emp2 = Employee('Shivani', 'Shukla', 125000)

Employee.set_raise_amt(1.05)
print(emp1.pay)
print(emp2.pay)

emp1.apply_raise()
emp2.apply_raise()

print(emp1.pay)
print(emp2.pay)