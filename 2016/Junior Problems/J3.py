ask = input('')
if ask[::-1]==ask:
    print(len(ask))
    exit()
index = 1
list1 = []
for y in range(1,len(ask)+1):
    for g in range(0,len(ask)+1):
        try:
            substring = ask[g:g+index]
            if len(substring)!=0:
                if substring[::-1]==substring:
                    if substring not in list1:
                        list1.append(substring)
        except ValueError:
            pass
    index+=1
max_len = 0
for t in list1:
    if len(t)>max_len:
        max_len=len(t)
print(max_len)
