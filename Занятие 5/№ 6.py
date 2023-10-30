def average():
    sum = 0.0
    count = 0
    while True:
        num = int(input('Введите число: '))
        if num == 0:
            break
        sum += num
        count += 1
    return sum / count
a = average()
print(a)