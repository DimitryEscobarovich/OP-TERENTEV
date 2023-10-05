def fibonachi(n):
    if n in (1, 2):
        return 1
    return fibonachi(n - 1) + fibonachi(n - 2)
a = 0
b = int(input())
for x in range(1, b+1):
    a += fibonachi(x)
print(a)