W = int(input())
H = float(input())
BMI = W/(H*H)
if BMI>25:
    print('Overweight')
elif BMI>=18.5 and BMI<=25:
    print('Normal weight')
else:
    print('Underweight')
