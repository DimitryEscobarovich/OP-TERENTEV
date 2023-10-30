# 1
def process_array():
    array = list(map(float, input('Введите элементы массива, разделенные пробелами: ').split()))
    min_abs_element = min(array, key=abs)
    print('Минимальный по модулю элемент: ', min_abs_element)
    print('Массив в обратном порядке: ', array[::-1])
a = process_array()
print(a)

# 2
def swap_arrays(A, B):
    print('Исходные массивы: ')
    print('A: ', A)
    print('B: ', B)

    A, B = B, A

    print('Преобразованные массивы: ')
    print('A: ', A)
    print('B: ', B)
a = swap_arrays(['1, 2, 3, 4, 5, 6,'] , ['7, 8, 9, 10, 11, 12'])
print(a)