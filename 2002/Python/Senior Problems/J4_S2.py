c = False
numerator = int(input(''))
denominator = int(input(''))
def gcf(num,den):
  if num>den:
    for g in range(den,0,-1):
      if num%g==0 and den%g==0:
        return g
  else:
    for g in range(num,0,-1):
      if num%g==0 and den%g==0:
        return g
if numerator==0:
  print(0)
  c = True
if numerator%denominator==0:
  print(numerator//denominator)
  c = True
if c==False:
  f = gcf(numerator,denominator)
  numerator = numerator//f
  denominator = denominator//f
  if numerator>denominator:
    num = numerator//denominator
    frac = numerator%denominator
    print(num,str(frac)+'/'+str(denominator))
    c = True
  if c==False:
    print(str(numerator)+'/'+str(denominator))
