# Символ @ является более простым способом создать замыкание

# 🔥 Важно! Функция декоратор должна быть определена в коде раньше, чем использована.
# В противном случае получим ошибку NameError.

"""
def main(func):
    def wrapper(*args, **kwargs):
        ...
        result = func(*args, **kwargs)
        ...
        return result

    return wrapper


@main
def my_func(data):
    ...
    return wrapper
"""

import time
from typing import Callable


def main(func: Callable):
    def wrapper(*args, **kwargs):
        print(f'Запуск функции {func.__name__} в {time.time()}')
        result = func(*args, **kwargs)
        print(f'Результат функции {func.__name__}: {result}')
        print(f'Завершение функции {func.__name__} в {time.time()}')
        return result

    return wrapper


@main
def factorial(n: int) -> int:
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


# Добавили декоратор @main к функции factorial.
# Необходимость в присваивании значения новой переменной отпала.

print(f'{factorial(1000) = }')
