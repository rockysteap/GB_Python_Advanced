# Декораторы functools

# Декоратор cache
# При необходимости кэширования данных рекомендуется использовать модуль
# functools cache, как более оптимальное решение из коробки.
"""
@cache
def my_func(data):
    ...
"""

from functools import cache


@cache
def factorial(n: int) -> int:
    print(f'Вычисляю факториал для числа {n}')
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


print(f'{factorial(10) = }')
# Вычисляю факториал для числа 10
# factorial(10) = 3628800

print(f'{factorial(15) = }')
# Вычисляю факториал для числа 15
# factorial(15) = 1307674368000

print(f'{factorial(10) = }')
# factorial(10) = 3628800

print(f'{factorial(20) = }')
# Вычисляю факториал для числа 20
# factorial(20) = 2432902008176640000

print(f'{factorial(10) = }')
# factorial(10) = 3628800

print(f'{factorial(20) = }')
# factorial(20) = 2432902008176640000
