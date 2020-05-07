def coin_flip(file_name):

    with open(file_name, 'r', encoding = 'UTF-8') as infile:
        lines = infile.readlines()

        for i in lines:
            head_num = i.count('h') + i.count('H')
            total = head_num + i.count('t') + i.count('T')
            heads_percentage = (head_num/total)*100

            if heads_percentage > 50:
                print(f'{head_num} heads ({heads_percentage:.1f}%)\nYou win!\n')
            else:
                print(f'{head_num} heads ({heads_percentage:.1f}%)\n')

        infile.close()

coin_flip('coin_flip_test.txt')