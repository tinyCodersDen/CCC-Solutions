# The problem name is "Time on task"
mins = int(input(''))
tasks = int(input(''))
list1 = []
for n in range(tasks):
    ask = int(input(''))
    list1.append(ask)
list1.sort()
c = 0
i = 0
for z in list1:
    if c>=mins:
        break
    else:
        if c+z>mins:
            break
        else:
            c+=z
            i +=1
print(i)
