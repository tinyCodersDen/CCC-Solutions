visited = [[-1, -6], [-1, -7], [0, -7], [1, -7], [2, -7], [3, -7], [4, -7], [5, -7], [6, -7], [7, -7], [7, -6], [7, -5], [7, -4], [7, -3], [6, -3], [5, -3], [5, -4], [5, -5], [4, -5], [3, -5], [3, -4], [3, -3], [2, -3], [1, -3], [0, -3], [0, -2], [0, -1]]
currCoord = [-1, -5]
danger = False #Stores whether the plan intersects itself
while 1: #Loop
  directions, numSpaces = input().split()
  if directions == 'q':
    break
  #Loop through the # of spaces to travel for each direction
  for i in range(int(numSpaces)):
    visited.append(currCoord)
    #Use math to arrive at the next coordinate
    if directions == 'd':
      currCoord = [currCoord[0], currCoord[1] - 1]
    elif directions == 'u':
      currCoord = [currCoord[0], currCoord[1] + 1]
    elif directions == 'l':
      currCoord = [currCoord[0] - 1, currCoord[1]]
    else:
      currCoord = [currCoord[0] + 1, currCoord[1]]
    
    #If the current coordinate is already visited
    if currCoord in visited:
      danger = True

  #Output
  if danger:
    print(currCoord[0], currCoord[1], "DANGER")
    break
  else:
    print(currCoord[0], currCoord[1], "safe")
