tenure = int(input("How many years have you been with the company? "))

if tenure < 10:
    print("You will receive a Christmas bonus of 50 pounds.")
elif 10 <= tenure < 20:
    print("You will receive a Christmas bonus of 100 pounds.")
else:
    print("You will receive a Christmas bonus of 150 pounds.")