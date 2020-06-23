q1 = int(input("Number to prime factorize: "))

for i in range(2, q1+1):
    count = 0
    while q1 % i == 0:
        q1 /= i
        count += 1
        if count > 1:
            print(f'{i}^{count}', end='')
            if q1 != 1:
                print('*', end='')

        elif q1 % i != 0:
            print(f'{i}', end='')
            if q1 != 1:
                print('*', end='')
