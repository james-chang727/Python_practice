"""This module defines a class that models an employee."""


class Employee:
    DEFAULT_STARTING_SALARY = 10000
    INCREMENT = 1000

    ## Constructs an Employee with a name and starting salary.
    def __init__(self, employee_name, employee_jobTitle):
        self.name = employee_name
        self.salary = Employee.DEFAULT_STARTING_SALARY
        self.jobTitle = employee_jobTitle

    # @return string representation of object.
    def __str__(self):
        return f'Name: {self.name}, salary: {str(self.salary)}'

    @property
    def jobTitle(self):
        return self._jobTitle

    @jobTitle.setter
    def jobTitle(self, jobName):
        if len(jobName) < 5 or (i.isdigit for i in jobName) == True:
            raise TypeError("Job Title should be longer or no digits in description!")
        self._jobTitle = jobName

    # name property allows get/set access to Employee's name value.
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

    ## salary property allows get/set access to Employee's salary.
    #  salary will be set to zero if there is an attempt to reduce
    #  it below zero.
    #
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salaryAmount):
        if salaryAmount >= 0:
            self._salary = salaryAmount
        else:
            self._salary = 0

    ## Promotes the employee by increasing the salary by INCREMENT.
    def promote(self):
        self.salary += Employee.INCREMENT

    ## Demotes the employee by decreasing the salary by INCREMENT.
    def demote(self):
        self.salary -= Employee.INCREMENT

    ## Raises the salary of the employee by the amount passed as a parameter.    
    # @param pay_rise the amount by which the the salary should be raised.
    #
    def raise_salary_by(self, pay_rise):
        if pay_rise > 0:
            self.salary += pay_rise

    ## Determines if this employee is equal to another employee.
    #  @param rhsValue the right-hand side employee.
    #  @return True if the names and the salaries are equal.
    #  @exception TypeError if the objects being compared are not
    #             the same type.
    #            
    def __eq__(self, rhsValue):
        if isinstance(rhsValue, Employee):
            return (self.name == rhsValue.name and
                    self.salary == rhsValue.salary)
        else:
            raise TypeError("Argument must be an Employee object.")
