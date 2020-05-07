tri_num = int(input("Enter the number of lines for the triangle: "))

# triangle of stars of a height given by the user
for i in range(tri_num+1):
    print("\t" + "*" * i)

print("\n")

# triangle of stars of a height upside down
for i in range(tri_num+1):
    print("\t" + "*" * (tri_num - i))

print("\n")

# isosceles triangle: print an upside down height triangle with space
for i in range(tri_num+1):
    print("\t" + " " * (tri_num - i), end = "")
    print("*" * (2*i + 1))
