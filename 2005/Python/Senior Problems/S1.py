dict1 = {2:['A','B','C'],3:['D','E','F'],4:['G','H','I'],5:['J','K','L'],6:['M','N','O'],7:['P','Q','R','S'],8:['T','U','V'],9:['W','X','Y','Z']}
for t in range(int(input())):
    n = input()
    n = n.replace('-','')
    for k,v in dict1.items():
        for t in v:
            n = n.replace(t,str(k))
    print(n[0:3]+'-'+n[3:6]+'-'+n[6:10])
