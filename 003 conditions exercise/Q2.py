age = int(input("Enter your age:"))
crim = str(input("Do you have a criminal record (y/n):"))
age_jury = 18 <= age <= 65

if age_jury and crim == "n":
    print("You are required to do jury service.")
elif not age_jury or crim == "y":
    print("You are excluded from jury service.")
elif crim != "y" or "n":
    print("Incorrect input.")
