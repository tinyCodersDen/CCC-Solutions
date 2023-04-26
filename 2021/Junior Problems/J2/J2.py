numbers = []
names = []
ask = int(input(''))
for u in range(ask):
    name = input('')
    bid = int(input(''))
    names.append(name)
    numbers.append(bid)
for a,q in enumerate(numbers):
    if q==max(numbers):
        print(names[a])
        exit()
