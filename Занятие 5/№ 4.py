def calculate_days(x, y):
    day = 1
    while x < y:
        x *= 1.1
        day += 1
    print(day)
calculate_days(10, 20)