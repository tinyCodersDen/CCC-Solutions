h = int(input(''))
max_t = int(input(''))
t = 1
for z in range(max_t):
    a = (-6*t**4) + (h*t**3) + (2*t**2) + t
    if a<=0:
        print('The balloon first touches ground at hour:')
        print(t)
        break
    if t == max_t:
        print('The balloon does not touch ground in the given time.')
    t+=1
