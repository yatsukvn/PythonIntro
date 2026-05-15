# 1. Присвойте двум переменным любые числовые значения.
a = 123
b = 234

# 2. Используя переменные из п. 1, с помощью оператора and составьте два сложных
#    логических выражения, одно из которых дает истину, другое – ложь

must_true = b > a and a < b
must_false = a < b and b < a

print('\nОператор and ')
print(f'must_true = b > a and a < b - {must_true}, must_false = a < b and b < a - {must_false}')

# 3. Аналогично выполните п. 2, но уже с оператором or.

must_true = b > a or a < b
must_false = a > b or b < a

print('\nОператор or ')
print(f'must_true = b > a or a < b - {must_true}, must_false = a > b or b < a - {must_false}')


# 4. Попробуйте использовать в логических выражениях переменные строкового типа.
#    Объясните результат.

c = 'string'
d = 'other string'

must_true = c > d
print('\nЛогические выражения переменных строкового типа ')
print(f'must_true = c > d = {must_true}')

# В языке Python это выражение сравнивает две строки лексикографически (по алфавиту)
# на основе числовых значений символов в кодировке Unicode.

n1 = int(input('Введите первое число:'))
n2 = int(input('Введите второе число:'))

print(f'Первое число {n1} {"больше" if n1 > n2 else "меньше"} второго числа {n2}')
