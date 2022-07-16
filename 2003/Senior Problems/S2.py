l = ['a','e','i','o','u']
for t in range(int(input())):
    verses = []
    for h in range(4):
        letter = input('').split(' ')[-1]
        f = ''
        for a in reversed(letter):
            f = a+f
            if a.lower() in l:
                break
        verses.append(f)
    verses[0],verses[1],verses[2],verses[3] = verses[0].lower(),verses[1].lower(),verses[2].lower(),verses[3].lower()
    if verses[0]==verses[1]==verses[2]==verses[3]:
        print('perfect')
    elif verses[0]==verses[1] and verses[2]==verses[3]:
        print('even')
    elif verses[0]==verses[2] and verses[1]==verses[3]:
        print('cross')
    elif verses[0]==verses[3] and verses[1]==verses[2]:
        print('shell')
    else:
        print('free')
