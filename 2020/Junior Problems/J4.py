list1 = []
for x in range(2):
    ask = input("")
    list1.append(ask)
shifts = []
string1 = list1[1]
for a in range(len(list1[1])):
    string1 += string1[0]
    string1 = string1[1:]
    shifts.append(string1)
for y in shifts:
    if y in list1[0]:
        print('yes')
        exit()
print('no')
