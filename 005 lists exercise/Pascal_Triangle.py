# Fills Pascal's triangle into the given 2D list up to the size of that list.

def fill_in(triangle):
    for i in range(len(triangle)):
        triangle[i] = [0] * (i + 1)  # create an empty row
        triangle[i][0] = 1
        triangle[i][i] = 1
        for j in range(1, i):
            # triangle[i][j] = (value above and left) + (value above)
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]


# Prints a 2D list with one row on each line with elements separated by spaces.
def print_nice(triangle):
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            print(triangle[i][j], end=" ")
        print()


def main():
    triangle = [0] * 11
    fill_in(triangle)
    print_nice(triangle)


main()
