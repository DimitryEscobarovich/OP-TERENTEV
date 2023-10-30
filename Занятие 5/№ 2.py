def smallest_divisor(n):
    for i in range(2, n):
        if n % i == 0:
            return i
        print(n)
a = smallest_divisor(10)
print(a)