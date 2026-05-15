# Напишите программу по следующему описанию.
# В основной ветке программы вызывается функция cylinder(), которая
# вычисляет площадь цилиндра. В теле cylinder определена функция circle, вычисляющая
# площадь круга по формуле πr**2. В теле cylinder у пользователя спрашивается, хочет ли он
# получить только площадь боковой поверхности цилиндра, которая вычисляется по формуле
# 2πrh, или полную площадь цилиндра. В последнем случае к площади боковой поверхности
# цилиндра должен добавляться удвоенный результат вычислений функции circle().
#
# Внимание! Ещё пока не знаем про оператор return
import math

cylinder_value = 0
lateral_surface_value = 0

r = 10
h = 40

def cylinder():
    def circle():
        global cylinder_value
        cylinder_value = math.pi * r ** 2

    def lateral_surface():
        global lateral_surface_value
        lateral_surface_value = 2 * math.pi * r * h

    result = int(input('Введите:\n1 - чтобы получить только площадь боковой поверхности цилиндра,\n2 - чтобы получмть полную площадь цилиндра\n> '))
    match result:
        case 1:
            lateral_surface()
            print(f'Результат: {lateral_surface_value:.2F}')
        case 2:
            lateral_surface()
            circle()
            print(f'Результат: {lateral_surface_value + 2 * cylinder_value:.2F}')
        case _:
            print('Неверный ввод')

cylinder()
