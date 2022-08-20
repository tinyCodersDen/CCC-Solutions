time = {'a': 1, 'b': 2, 'c': 3, 'd': 1, 'e': 2, 'f': 3, 'g': 1, 'h': 2, 'i': 3, 'j': 1, 'k': 2, 'l': 3, 'm': 1, 'n': 2, 'o': 3, 'p': 1, 'q': 2, 'r': 3, 's': 4, 't': 1, 'u': 2, 'v': 3, 'w': 1, 'x': 2, 'y': 3, 'z': 4}
groups = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
while True:
  h = input('')
  if h=='halt':
    break
  ans = 0
  for e,j in enumerate(h):
    ans+=time[j]
    if e!=len(h)-1:
      group1 = 0
      group2 = 0
      for q,t in enumerate(groups):
        if j in t:
          group1 = q
          break
      for q,t in enumerate(groups):
        if h[e+1] in t:
          group2 = q
          break
      if group1==group2:
        ans+=2
  print(ans)
