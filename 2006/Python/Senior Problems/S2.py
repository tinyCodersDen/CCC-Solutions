i = input()
cipher = input()
dict1 = {}
for e,t in enumerate(i):
    dict1[cipher[e]] = t
code = input()
answer = ''
for t in code:
    try:
        answer+=dict1[t]
    except:
        answer+='.'
print(answer)
