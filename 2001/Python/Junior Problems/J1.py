H = int(input())
for n in range(1,H,2):
    string = ('*'*n)+(' '*((H*2)-(n*2)))+('*'*n)
    print(string)
for n in range(H,0,-2):
    string = ('*'*n)+(' '*((H*2)-(n*2)))+('*'*n)
    print(string)
