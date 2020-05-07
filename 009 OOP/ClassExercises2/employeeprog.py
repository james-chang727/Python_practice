"""This program uses the Employee class to manage an Employee."""

from employee_module import Employee


def main():
    name = input("\n\tEnter the employee's name: ")
    jobTitle = input ("\tEnter the employee's job title: ")
    employee = Employee(name, jobTitle)

    selection = 'a'

    while selection != 'q':
        print("\tType: ")
        print("\t\tp - to promote the employee")
        print("\t\td - to demote the employee")
        print("\t\tr - to raise the employee's salary by a given amount")
        print("\t\tv - to view the employee's details")
        print("\t\tq - to quit\n")

        selection = input("\tEnter selection: ")[0]
        if selection == 'p':
            employee.promote()
        elif selection == 'd':
            employee.demote()
        elif selection == 'r':
            rise = int(input("\tEnter amount of rise: "))
            employee.raise_salary_by(rise)
        elif selection == 'v':
            print(employee)

    print("\tPROGRAM ENDED\n")


if __name__ == "__main__":
    main()
