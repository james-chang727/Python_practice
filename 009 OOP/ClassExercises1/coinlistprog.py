from coin_module import Coin

c = Coin()

Coin.heads_so_far = 0
Coin.tails_so_far = 0

print('coins:', end=' ')

for i in range(20):
    print(Coin(), end=' ')
else:
    print(f'\n\nHeads: {c.get_heads_so_far()}')
    print(f'Tails: {c.get_tails_so_far()}')

