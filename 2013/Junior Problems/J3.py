# The problem name is "From 1987 to 2013"
ask = int(input(''))
check = False
while True:
    ask+=1
    string_ask = str(ask)
    t = ''
    check = False
    for i in string_ask:
        if i not in t:
            t+=i
        else:
            check = True
    if check == False:
        print(ask)
        break
