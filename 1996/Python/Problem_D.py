for h in range(int(input(''))):
    g = input('')
    m = g[:-1].split('+')
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    m2 = []
    for s in m:
      int_val = 0
      for i in range(len(s)):
          if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
              int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
          else:
              int_val += rom_val[s[i]]
      m2.append(int_val)
    number = sum(m2)
    if number>1000:
        print(g+'CONCORDIA CUM VERITATE')
        continue
    numerals = { 1 : "I", 4 : "IV", 5 : "V", 9 : "IX", 10 : "X", 40 : "XL",50 : "L", 90: "XC", 100 : "C", 400 : "CD", 500 : "D", 900 : "CM", 1000 : "M" }
    roman = ''

    for k, v in sorted(numerals.items(), reverse=True):
        while number >= k:
            roman += v
            number -= k

    print(g+roman)
