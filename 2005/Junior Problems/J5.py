while True:
  k = input()
  if k=='X':
    break
  for t in range(len(k)):
    k = k.replace('ANA','A')
    k = k.replace('BAS','A')
  if k=='A':
    print('YES')
  else:
    print('NO')
