n = int(input(''))
boards = input('').split(' ')
l = [0]*2001
f = [0]*4002
for board in boards:
    l[int(board)]+=1
for y in range(0,len(l)-1):
    for t in range(y,len(l)):
        if y==t:
            f[t+y]+=l[y]//2
        else:
            f[t+y]+=min([l[t],l[y]])
longest=0
size_of_longest=0
for a in f:
    if a>longest:
        longest=a
        size_of_longest=1
    elif a==longest:
        size_of_longest+=1
print(longest,size_of_longest)
