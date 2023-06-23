class Employee:
    def raisee(self):
        raise_rate = 0.1
        result = 100 + 100 * raise_rate
        print("Employee:", result)

# Employee class representing a generic employee with a raisee method.

class CompEng(Employee):
    def raisee(self):
        raise_rate = 0.2
        result = 100 + 100 * raise_rate
        print("CompEng:", result)

# CompEng class inheriting from Employee and overriding the raisee method.
# Represents an employee in the Computer Engineering department.

class EEE(Employee):
    def raisee(self):
        raise_rate = 0.3
        result = 100 + 100 * raise_rate
        print("EEE:", result)

# EEE class inheriting from Employee and overriding the raisee method.
# Represents an employee in the Electrical and Electronics Engineering department.


e1 = Employee()
ce = CompEng()
eee = EEE()

# Creating instances of the Employee, CompEng, and EEE classes.

employee_list = [ce, eee]

# Creating a list to store instances of employees.

for employee in employee_list:
    employee.raisee()

# Looping through the employee_list and calling the raisee method for each employee.

