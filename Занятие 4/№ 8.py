N = int(input('Введите число: '))
styp = ' '
if N <= 9:
    for i in range(1, N+1):
        styp += str(i)
        print(styp)