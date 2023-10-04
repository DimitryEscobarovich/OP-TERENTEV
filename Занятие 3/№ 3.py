n = int(input('Введите количество минут: '))
hours = n // 60
minutes = n % 60
if hours > 23:
    hours = hours % 24
print("На электронных часах будет показываться", hours, "часов", minutes, "минут.")