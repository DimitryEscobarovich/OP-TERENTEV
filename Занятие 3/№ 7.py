def year(a):  
    if a % 400 == 0 or a % 4 == 0 and a % 100 != 0:
        print('Год высокосный')
    else:
        print('Год не высокосный')
a = int(input('Введите год: '))
year(a)