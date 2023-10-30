def count_numbers():
    count = 0
    while True:
        num = int(input('Введите число: '))
        if num == 0:
            break
        count += 1
    return count
a = count_numbers()
print(a)