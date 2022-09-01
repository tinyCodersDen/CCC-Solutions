l = []
s = []
while True:
  direction = input('')
  if direction=='R':
    l.insert(0,'LEFT')
  else:
    l.insert(0,'RIGHT')
  street = input('')
  if street!='SCHOOL':
    s.insert(0,street)
  else:
    s.append('HOME')
    break
for q,y in enumerate(l):
  if s[q]!='HOME':
    print('Turn',y,'onto',s[q],'street.')
  else:
    print('Turn',y,'into your HOME.')
