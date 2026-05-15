# Использование модуля module из файла module.py

from module import circle, triangle, rectangle

a = 12.34
b = 6.789
h = 2.3456
r = 5.6789012

print(f'circle = {circle(r)}')
print(f'triangle = {triangle(a,h)}')
print(f'rectangle = {rectangle(a,b)}')