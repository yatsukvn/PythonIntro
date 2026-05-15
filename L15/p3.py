# 3. Напишите программу, которая запрашивает у пользователя шесть вещественных чисел.
#    На экран выводит минимальное и максимальное из них, округленные до двух знаков
#    после запятой. Выполните задание без использования встроенных функций min и max.

numbers = []

for i in range(1, 7):
    numbers.append(float(input(f'Введите вещественное число № {i}: ')))

minimum = numbers[0]
maximum = numbers[0]
for i in range(0, 6):
    if numbers[i] < minimum:
        minimum = numbers[i]
    elif numbers[i] > maximum:
        maximum = numbers[i]

print(f'Minimum = {round(minimum,2)}, maximum = {round(maximum,2)}')