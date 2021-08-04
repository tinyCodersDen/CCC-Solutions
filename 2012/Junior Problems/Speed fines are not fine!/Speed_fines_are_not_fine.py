ask = int(input('Enter the speed limit: '))
ask2 = int(input('Enter the recorded speed of the car: '))
if ask2>ask:
    num = ask2-ask
    if num>=1 and num<=20:
        print('You are speeding and your fine is $100.')
        exit()
    if num>=21 and num<=30:
        print('You are speeding and your fine is $270.')
        exit()
    if num>=31:
        print('You are speeding and your fine is $500.')
        exit()
else:
    print('Congratulations, you are within the speed limit!')
    exit()
