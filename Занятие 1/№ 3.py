age = int(input('Сколько вам лет? '))
name = input('Как вас зовут? ')
if age > 0 and age < 75:
    if name != 'Иван':
        if age >= 16:
            print ('Поздравляем вы поступили во ВГУИТ')
        else:
            print ('Сначала нужно окончить школу!')
            print ('Вы должны ещё', 16 - age, 'лет учиться в школе')
    else:
        print ('Извините, но вас зовут Иван, вам нельзя поступить')
else:
    print ('Вы не проходите по первому условию')