for h in range(int(input(''))):
    l = int(input(''))
    s1 = 0
    for h in range(1,l):
        if l%h==0:
            s1+=h
    if s1==l:
        print(l,'is a perfect number.')
    elif s1<l:
        print(l,'is a deficient number.')
    else:
        print(l,'is an abundant number.')
