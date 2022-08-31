amount = int(input())
coins = []
for t in range(int(input())):
    coins.append(int(input()))
to_collect = 1 << amount
n = 0
b = False
while not to_collect & 1:
    collected = to_collect
    for coin in coins:
        collected |= to_collect >> coin
    if collected == to_collect:
        print('Roberta acknowledges defeat.')
        b = True
        break
    to_collect ^= collected
    n += 1
if not b:
    print('Roberta wins in',n,'strokes.')
