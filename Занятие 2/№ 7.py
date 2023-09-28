import math
x = float(input('Введите число x:'))
y = float(input('Введите число y:'))
z = float(input('Введите число z:'))
s = 5*math.atan(x)-1/4*math.acos(x)*(x+3*abs(x-y)+x**2)/(abs(x-y)*z+x**2)
print (s)