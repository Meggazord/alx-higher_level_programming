#!/usr/bin/python3

class Employee():

    raise_amount = 1.04

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def apply_raise(self):
        self.salary = self.salary * self.raise_amount


emp_1 = Employee("Karim", 200000)
emp_2 = Employee("Test", 10000)

emp_1.raise_amount = 1.05
Employee.raise_amount = 1.06


print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
