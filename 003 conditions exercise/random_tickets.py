import random
lottery_num = random.randrange(1, 4)

if int(lottery_num) == 1:
    print("You have won {} ticket.".format(lottery_num))
else:
    print("You have won {} tickets.".format(lottery_num))