def f_sum(a):
    sum=0
    f=1
    for i in range(1, a + 1):
        f *= i
        sum += f
    return sum
a = int(input('Введите число: '))
result = f_sum(a)
print('Сумма факториалов = ', result)