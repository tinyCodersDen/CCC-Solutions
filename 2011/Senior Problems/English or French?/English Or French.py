x = int(input())
number_of_s = 0
number_of_t = 0
for i in range(x):
    v = input()
    for a in v:
        if a=='t' or a=='T':
            number_of_t+=1
        elif a=='s' or a=='S':
            number_of_s+=1
if number_of_t>number_of_s:
    print('English')
else:
    print('French')
