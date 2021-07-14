print('How many antennas?')
ask1 = int(input(''))
print('How many eyes?')
ask2 = int(input(''))
if ask1>=3 and ask2<=4:
    print('TroyMartian')
if ask1<=6 and ask2>=2:
    print('VladSaturnian')
if ask1<=2 and ask2<=3:
    print('GraemeMercurian')
