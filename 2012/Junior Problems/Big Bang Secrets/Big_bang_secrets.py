import string
k = int(input(''))
string1 = input('')
list1 = list(string.ascii_uppercase)
p = 1
newstring = ''
for i in string1:
    s = 3*p+k
    try:
        new = list1[list1.index(i)-s]
        newstring+=new
        p+=1
    except IndexError:
        s = 26-(list1.index(i)+1)
        new = list1[s]
        newstring+=new
        p+=1
print(newstring)
