directions = []
streets = []
while True:
  direction = input('')
  street = input('')
  if direction=='L':
    directions.insert(0,'RIGHT')
  elif direction=='R':
    directions.insert(0,'LEFT')
  streets.append(street)
  if street == 'SCHOOL':
    break
streets = list(reversed(streets))
streets.pop(0)
streets.append('HOME')
for n in range(0,len(directions)):
  if streets[n]!='HOME':
    print('Turn',directions[n],'onto',streets[n],'street.')
  else:
    print('Turn',directions[n],'into your HOME.')
