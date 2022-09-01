rivers = []
for t in range(int(input())):
    rivers.append(int(input()))
while True:
    command = int(input())
    if command==77:
        for e,t in enumerate(rivers):
           t = int(round(t,0))
           t = str(t)
           rivers[e] = t
        print(' '.join(rivers))
        break
    elif command==99:
        index = int(input())
        percentage = int(input())/100
        rivers.insert(index,rivers[index-1]*(1-percentage))
        rivers[index-1] = rivers[index-1]*percentage
    elif command==88:
        index = int(input())-1
        rivers[index] = rivers[index+1]+rivers[index]
        rivers.pop(index+1)
