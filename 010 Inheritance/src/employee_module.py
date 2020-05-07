###  This module defines a class that models an employee.
#

from date_module import Date

## An employee has a name and a start date. 
#
class Employee:
    
    ## Constructs an Employee with a name and start date.
    #  @param employee_name the name of the employee.
    #  @param start_date the date the employee started their employment
    #
    def __init__(self, employee_name="No name", day = 1, month = 1,
                 year = 2000) :
            self.name = employee_name
            self.date = Date(day, month, year)
            
    ##    
    # @return string representation of object.
    #
    def __str__(self):
        return "Name: " + self.name + ", start date: " + str(self.date)

    ## name property allows get/set access to Employee's name value.
    #  name must not be whitespace else a ValueError is raised.
    #
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, theName):
        if len(theName.strip()) != 0:
            self._name = theName
        else:
            raise ValueError("Invalid name: " + name)
        
    ## Determines if this employee is equal to another employee.
    #  @param otherEmployee the employee inside the brackets.
    #  @return True if the names and the start dates are equal.
    #  @exception TypeError if the objects being compared are not
    #             the same type or the object being compared is empty.
    #            
    def __eq__(self, otherEmployee) :
        if otherEmployee is None or not isinstance(otherEmployee, Employee) :
            raise TypeError("Argument must be an Employee object and cannot be null.")
        else :
            return (self.name == otherEmployee.name and
              self.date == otherEmployee.date)
            



# def main() :
#     # a simple main function to test this class
#     employee1 = Employee("Bart Simpson", 30, 11, 2018)
#     employee2 = Employee("Marge Simpson", 31, 1, 2018)
#     employee3 = Employee("Lisa Simpson", 15, 6, 2016)
# 
#     print("First Employee: " + str(employee1))
#     print("Second Employee: " + str(employee2))
#     print("Third Employee: " + str(employee3))
#     print("First Employee and Second Employee are ", end="")
#     if employee1 != employee2 :
#         print("not ", end="")
#     print("equal.")
# 
# if __name__ == '__main__':
#     main()         