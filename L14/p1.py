# Напишите программу, в которой определена функция int_test, имеющая один параметр. Функция
# проверяет, можно ли переданное ей значение преобразовать к целому числу. Если можно,
# возвращает логическое True. Если нельзя – False.


def int_test(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


s = input('Введите число: ')
if int_test(s):
    print(f'{int(s) + 10}')
