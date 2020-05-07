cel_temp = int(input("Enter the first amount in Celsius: "))
line_num = int(input("Enter the number of lines for the table: "))
step_temp = int(input("Enter a whole number difference between lines in Celsius: "))

print("\n\t\tCELSIUS\t\tFAHRENHEIT")

for i in range(line_num):
    print("\t\t {}\t\t\t{:.1f}".format(cel_temp, 1.8*cel_temp + 32 ))
    cel_temp += step_temp
