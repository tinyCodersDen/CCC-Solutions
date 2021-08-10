l = []
numbers = []
while True:
    ask = input('')
    if ask=='99999':
        for h in range(len(l)):
            print(l[h],numbers[h])
        exit()
    sum1 = int(ask[0])+int(ask[1])
    if sum1==0:
        l.append(l[-1])
        numbers.append(ask[2:])
    else:
        g = sum1/2
        if g == int(g):
            l.append('right')
            numbers.append(ask[2:])
        elif g != int(g):
            l.append('left')
            numbers.append(ask[2:])
