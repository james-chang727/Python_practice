def flip_lines(file_name):

    with open(file_name, "r", encoding="UTF-8") as infile:
        lines = infile.readlines()
        my_order = [1, 0, 3, 2]
        my_lines = [lines[i] for i in my_order]

        for i in my_lines:
            print(i.rstrip())

    infile.close()

flip_lines('flip_lines_test.txt')
