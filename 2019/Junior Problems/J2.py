list1 = []
num = int(input(""))
for x in range(num):
    ask = input("")
    list1.append(ask)
for x in list1:
    l = x.split(" ")
    string1 = ''
    for y in range(int(l[0])):
        string1+=l[1]
    print(string1)
