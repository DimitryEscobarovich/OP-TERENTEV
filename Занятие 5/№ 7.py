def most_frequent():
    from collections import defaultdict
    counts = defaultdict(int)
    while True:
        num = int(input('Введите число: '))
        if num == 0:
            break
        counts[num] += 1
    most_frequent_num = max(counts, key=counts.get)
    return most_frequent_num, counts[most_frequent_num]
a = most_frequent()
print(a)