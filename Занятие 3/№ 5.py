def min(a, b, c):
    min = a
    if b < min:
        min = b
    if c < min:
        min = c
    print('Наименьшее число: ', min)
a = int(input('Введите первое число '))
b = int(input('Введите второе число '))
c = int(input('Введите третье число '))
min(a, b, c)