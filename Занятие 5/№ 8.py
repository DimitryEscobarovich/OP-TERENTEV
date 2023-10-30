def max_equal_sequence():
    max_count = 0
    count = 1
    prev_num = int(input('Введите число: '))
    while True:
        num = int(input('Введите число: '))
        if num == 0:
            break
        if num == prev_num:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 1
        prev_num = num
    max_count = max(max_count, count)
    return max_count
a = max_equal_sequence()
print(a)