def pattern_generator(n, k, s):
    if n == 0 and k == 0:
        print (s)
        return
    if n == 0:
        return
    else:
        if k >= 1:
            pattern_generator(n-1, k-1, s+"1")
        pattern_generator(n-1, k, s+"0")


first = int(input())
all_inputs = []
for i in range(first):
    all_inputs.append(input().split())
for i in range(len(all_inputs)):
    print ("The bit patterns are")
    n = int(all_inputs[i][0])
    k = int(all_inputs[i][1])
    pattern_generator(n, k, "")
