import math
x = float(input('Введите число x:'))
y = float(input('Введите число y:'))
z = float(input('Введите число z:'))
s = math.log1p(pow(y,-math.sqrt(abs(x))))*(x-y/2)+math.sin(math.atan(z))**2
print (s)