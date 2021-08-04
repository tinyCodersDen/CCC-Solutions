# The problem name is "What is n, Daddy?"
num = int(input(''))
l = []
for x in range(num):
    y = num-x
    if x<=5 and y<=5:
        if [y,x] not in l and [x,y] not in l:
            l.append([x,y])
print(len(l))
