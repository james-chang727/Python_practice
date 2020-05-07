year = int(input("Enter a year to check if it is a leap year: "))

leap_year = "{} is a leap year".format(year)
not_leap_year = "{} is not a leap year.".format(year)

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(leap_year)
        else:
            print(not_leap_year)
    else:
        print(leap_year)
else:
    print(not_leap_year)
