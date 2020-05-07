def squareString(a, b):
    if b > a:
        stk = []
        for i in range(a, b+1):
            stk.append(str(i))

        for i in range(len(stk)):
            final_list = stk[i:] + stk[:i]
            str_list = ''.join(str(i) for i in final_list)
            print(str_list)

    else:
        print('Invalid input')

squareString(3, 9)
