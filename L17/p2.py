# 2. Напишите программу, которая запрашивает у пользователя границы диапазона и какое
#    (целое или вещественное) число он хочет получить. Выводит на экран подходящее
#    случайное число.
import random

def random_int(l, u):
    return random.randint(l, u + 1)

def random_float(l, u):
    return random.random() * (u - l) + l

lower_limit = input('Введите нижнюю границу диапазона: ')
upper_limit = input('Введите верхнюю границу диапазона: ')
what_number = 0

try:
    what_number = int(input('1 - целое, 2 - вещественное: '))

    match what_number:
        case 1:
            lower = int(lower_limit)
            upper = int(upper_limit)
            # если перепутали границы диапазона для целых чисел
            if lower > upper:
                lower, upper = upper, lower
            print(f'Случайное целое число: {random_int(int(lower_limit), int(upper_limit))}')
        case 2:
            lower = float(lower_limit)
            upper = float(upper_limit)
            # если перепутали границы диапазона для вещественных чисел
            if lower > upper:
                lower, upper = upper, lower
            print(f'Случайное вещественное число: {random_float(float(lower_limit), float(upper_limit))}')
        case _:
            print('Должно быть 1 или 2')
except ValueError:
    print(f'Неверные границы диапазона, нижняя = {lower_limit}, верхняя = {upper_limit} или неверно задан тип числа: {what_number}')


