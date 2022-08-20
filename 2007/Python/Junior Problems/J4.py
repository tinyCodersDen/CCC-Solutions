w1 = input()
w2 = input()
dict1 = {}
dict2 = {}
for i in range(len(w1)):
  if w1[i] == ' ':
      continue
  elif w1[i] in dict1:
      dict1[w1[i]] += 1
  else:
      dict1[w1[i]] = 1

for j in range(len(w2)):
  if w2[j] == ' ':
      continue
  elif w2[j] in dict2:
      dict2[w2[j]] += 1
  else:
      dict2[w2[j]] = 1
if dict1 == dict2:
  print('Is an anagram.')
else:
  print('Is not an anagram.')
