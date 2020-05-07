def is_magic_square(lis):
    n = len(lis)
    magic_sum = sum(lis[0])

    # calculate row sum
    for i in range(n):
        if sum(lis[i]) != magic_sum:
            return False

    # calculate column sum
    column_sum = 0

    for i in range(n):
        for j in range(n):
            column_sum += lis[j][i]
        if column_sum != magic_sum:
            return False
        else:
            column_sum = 0

    # calculate diagonals
    sum_diagonal1 = 0
    sum_diagonal2 = 0

    for i in range(n):
        sum_diagonal1 += lis[i][i]
        sum_diagonal2 += lis[i][n - i - 1]
    if sum_diagonal1 != magic_sum or sum_diagonal2 != magic_sum:
        return False

    return True


list1 = [[2, 7, 6],
         [9, 5, 1],
         [4, 3, 8]]
list2 = [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 1]]

print(is_magic_square(list1))
print(is_magic_square(list2))
