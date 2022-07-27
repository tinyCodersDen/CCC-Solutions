# perfect numbers between 1000 and 9999
for num in range(1000, 9999+1):
    s = {1}
    for factor in range(2, int(num**0.5)+1):
        if num % factor == 0:
            s.add(factor)
            s.add(num/factor)
    add = 0
    for c in s:
        add += c
    if add == num:
        print(num)

# integers that are equal to the sum of their digits cubed
for num in range(100, 999):
    count = 0
    number = str(num)
    for integer in number:
        count += (int(integer))**3
    if num == count:
        print(num, end=' ')
