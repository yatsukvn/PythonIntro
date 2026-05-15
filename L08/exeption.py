# Напишите программу, которая запрашивает ввод двух значений. Если хотя бы одно из них не
# является числом, то должна выполняться конкатенация, то есть соединение, строк. В остальных
# случаях введенные числа суммируются.

value_s1 = ''
value_s2 = ''

value_n1 = 0
value_n2 = 0

try:
    value_s1 = input('Введите первое значение: ')
    value_s2 = input('Введите второе значение: ')
    value_n1 = int(value_s1)
    value_n2 = int(value_s2)
except ValueError:
    value_n1 = value_s1
    value_n2 = value_s2
finally:
    print(f'Первое значение: {value_n1}')
    print(f'Второе значение: {value_n2}')
    print(f'Результат: {value_n1+value_n2}')