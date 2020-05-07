age = int(input("Enter your age: "))
price = 6

if age < 16 or age > 60:
    print("Your ticket costs {0:4.2f} pounds.".format(price/3))
else:
    print("Your ticket costs {0:4.2f} pounds.".format(price))
