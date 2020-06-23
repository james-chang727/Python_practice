class Employee:

    # These are class variables
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay): # These are instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # Dunders are special methods surrounded by double underscorers
    # __repr__: unambiguous representation of the object, used for debugging
    def __repr__(self):
        # return a string that could be used to recreate the object
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    # __str__: readable representation, used for display to end users
    def __str__(self):
        return "{} - {}" .format(self.fullname(), self.email)

    @classmethod # Applies the attribute to all class instances
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod # Doesn't take in any instances or class on default
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
           return False
        return True

emp_1 = Employee('James', 'Chang', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

# Python looks for __init__ method in the Developer class, then walk up the chain of inheritance,
# which is called the method resolution order, can be looked up through print(help())
class Developer(Employee):
    # Change in subclasses to variables don't affect the parent class
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        # super(): calling parent __init__ method in a more maintainable way
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        # We generally don't use mutable data types in the arguments
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    # Method that gives the manager class the ability to append a new employee
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1 = Developer('James', 'Chang', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

# Tells us if an object is an instance of a class
# isinstance()
# If the former class is a subclass of the latter
# issubclass()


