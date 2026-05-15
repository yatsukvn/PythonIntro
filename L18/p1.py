# 1. Напишите программу, которая запрашивает с ввода восемь чисел, добавляет их в список.
#    На экран выводит их сумму, максимальное и минимальное из них. Для нахождения
#    суммы, максимума и минимума воспользуйтесь встроенными в Python функциями sum(),
#    max() и min().

numbers = []

for i in range(1, 9):
    numbers.append(int(input(f'Введите число № {i}: ')))

summa = sum(numbers)
minimum = min(numbers)
maximum = max(numbers)

print(f'Итоговый список: {numbers}')
print(f'Сумма: {summa}')
print(f'Минимум: {minimum}')
print(f'Максимум: {maximum}')