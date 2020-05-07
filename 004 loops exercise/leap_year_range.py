start_year = int(input("Enter start year: "))
end_year = int(input("Enter end year: "))

print("Here is a list of leap years between {} and {}:".format(start_year, end_year))
print("\n")

count = 0

for year in range(start_year, end_year):

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        if end_year - year <= 4:
            print(year, end=".")
        else:
            print(year, end=", ")
            count += 1
            if count == 10:
                print("\n")
                count = 0