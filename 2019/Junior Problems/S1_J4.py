l = [1,2,3,4]
x = input('')
for g in x:
    if g=='V':
        l[0],l[1] = l[1],l[0]
        l[2],l[3] = l[3],l[2]
    if g=='H':
        l[1],l[3] = l[3],l[1]
        l[0],l[2] = l[2],l[0]
print(l[0],l[1])
print(l[2],l[3])
