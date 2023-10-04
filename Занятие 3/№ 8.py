def numbers(z, x, c):
    if z == x and x == c and z == c:
        print('3')
    elif z == x or x == c:
        print('2')
    else:  
        print('0')
z = int(input('Введите первое число: '))
x = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
numbers(z, x, c)