for _ in range(int(input())):
    n = int(input())
    pairs = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            pairs.append(i + n // i)
            pairs.append(n // i - i)
    for num in pairs:
        if pairs.count(num) != 1:
            print(f"{n} is nasty")
            break
    else:
        print(f"{n} is not nasty")
