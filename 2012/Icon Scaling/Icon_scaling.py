string1,string2,string3 = '','',''
ask = int(input(''))
string1+='*'*ask
string1+='x'*ask
string1+='*'*ask
string2+=' '*ask
string2+='x'*ask
string2+='x'*ask
string3+='*'*ask
string3+=' '*ask
string3+='*'*ask
for j in range(ask):
    print(string1)
for j in range(ask):
    print(string2)
for j in range(ask):
    print(string3)
