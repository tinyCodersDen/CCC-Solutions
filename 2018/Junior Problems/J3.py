inputs = []
ask = input('')
inputs=ask.split(' ')
inputs = [int(x) for x in inputs]
count = 0
string1 = ''
for x in range(5):
    for y in range(5):
        if x==y:
            string1+='0 '
        else:
            if x<y:
                for t in inputs[x:y]:
                    count+=t
            else:
                for t in inputs[y:x]:
                    count+=t
            string1=string1+str(count)+' '
            count = 0
    print(string1)
    string1 = ''
