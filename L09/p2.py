# 2. Усовершенствуйте предыдущую программу (p1.py), обработав исключение ValueError,
#    возникающее, когда вводится не целое число.

try:
    age = int(input('Ваш возраст: '))
except ValueError:
    age = 0
finally:
    print('Рекомендовано:', end=' ')
    if 3 <= age < 6:
        print('"Заяц в лабиринте"')
    elif 6 <= age < 12:
        print('"Марсианин"')
    elif 12 <= age < 16:
        print('"Загадочный остров"')
    elif 16 <= age:
        print('"Поток сознания"')
    else:
        print('нет')
