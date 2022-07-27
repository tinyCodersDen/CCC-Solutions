for j in range(int(input(''))):
    l = input('').split(' ')
    for e,j in enumerate(l):
        if len(j)==4:
            l[e] = '****'
    print(' '.join(l))
