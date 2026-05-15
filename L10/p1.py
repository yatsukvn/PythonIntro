# 1. Измените последний код из урока так, чтобы переменная total не могла уйти в минус.
#    Например, после предыдущих вычитаний ее значение стало равным 25. Пользователь
#    вводит число 30. Однако программа не выполняет вычитание, а выводит сообщение о
#    недопустимости операции, после чего осуществляет выход из цикла.

# total = 100
# while total > 0:
#  n = int(input())
#  total -= n
# print("Ресурс исчерпан")

def print_values(value_n, value_total):
    print(f'n = {value_n}, total = {value_total}')

total = 100
n = 0
print_values(n, total)

while total > 0:
    n = int(input('Введите новое значение n: '))
    print_values(n, total)
    if n > total:
        print('Недопустимая операция: n > total')
        break
    total -= n