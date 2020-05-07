# This program calculates how old someone will be in a given year and month,
# after prompting for the current year, month and user's age.

def main():
    year_now = int(input("Enter the current year then press RETURN: "))
    int(input("Enter the current month (a number from 1 to 12): "))
    age_now = int(input("Enter your current age in years: "))
    month_born = int(input("Enter the month in which you were born (a number from 1 to 12): "))
    another_year = int(input("Enter the year in which you wish to know your age: "))
    another_month = int(input("Enter the month in this year: "))
    another_age = another_year - (year_now - age_now)

    if another_month < month_born:
        another_age -= 1
        another_age_months = 12 + another_month - month_born
    else:
        another_age_months = another_month - month_born

    if another_age_months == 1:
        print("Your age in {}/{}: {} years and 1 month".format(another_month, another_year, another_age))
    elif another_age_months == 0:
        print("Your age in {}/{}: {} years".format(another_month, another_year, another_age))
    else:
        print("Your age in {}/{}: {} years and {} months".format(another_month, another_year, another_age, another_age_months))

if __name__ == "__main__":
    main()