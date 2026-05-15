var_int = 10
var_float = 8.4
var_str = 'No'

var_big = var_int * 3.5
print(f'var_big = {var_big}')

var_big = var_float - 1
print(f'var_big = {var_big}')

var_a = var_int / var_float
var_b = var_big / var_float

print(f'var_a = {var_a}, var_b = {var_b}')

var_str = var_str * 2 + 'Yes' * 3

print(f'var_str = "{var_str}"')