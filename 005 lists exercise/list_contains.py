"""checks if list1 contains list2 in the same order"""

def contains(l1, l2):
    for i in range(len(l1) - len(l2) + 1):
        for j in range(len(l2)):
            if l1[i + j] != l2[j]:
                break
                '''exits j loop, starts again with the next value 
                of i in the first for loop'''
        else:
        # else statement is executed after the for loop falls through
            return True
    return False
    '''this statement is reached if "break" is reached by the last i, 
    the else statement is skipped if "break" is executed'''


list1 = [1, 6, 2, 1, 4, 1, 2, 1, 8]
list2 = [1, 2, 1]

print(contains(list1, list2))
