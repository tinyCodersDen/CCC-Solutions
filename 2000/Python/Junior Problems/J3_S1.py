m = int(input())
x = int(input())
y = int(input())
z = int(input())
i = 0
while True:
    x+=1
    m-=1
    i+=1
    if x == 35:
        m+=30
        x = 0
    if m<=0: break
    y+=1
    m-=1
    i+=1
    if y == 100:
        m+=60
        y = 0
    if m<=0: break
    z+=1
    m-=1
    i+=1
    if z == 10:
        m+=9
        z = 0
    if m<=0: break
print('Martha plays',i,'times before going broke.')
