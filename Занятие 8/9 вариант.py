# 1
def count_subtractions(n):
    steps = 0
    while n > 0:
        n -= sum(int(digit) for digit in str(n))
        steps += 1
    return steps
a = count_subtractions(1234)
print(a)

# 2
def calculate_arrays(A, B, C):
    for i, array in enumerate([A, B, C], start=1):
        product = 1
        sum_elements = 0
        for num in array:
            product *= num
            sum_elements += num
        average = sum_elements / len(array)
        print(f"Массив {i}:")
        print(f"Произведение элементов: {product}")
        print(f"Среднее значение: {average}")
a = calculate_arrays([1, 2], [3, 5], [6, 8])
print(a)