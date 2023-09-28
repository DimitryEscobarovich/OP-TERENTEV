import math
x = float(input('Введите число x:'))
y = float(input('Введите число y:'))
z = float(input('Введите число z:'))
s = (abs(math.cos(x)-math.cos(y))**(1+2*math.sin(y)**2))*(1+z+math.pow(z,2)/2+math.pow(z,3)/3+math.pow(z,4)/4)
print (s)