dict1 = {1:[461,431,420,0],2:[100,57,70,0],3:[130,160,118,0],4:[167,266,75,0]}
sum1 = 0
for g in range(4):
    h = int(input(''))
    sum1 += dict1[g+1][h-1]
print('Your total Calorie count is '+str(sum1)+'.')
