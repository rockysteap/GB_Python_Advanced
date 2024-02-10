# Декораторы functools

# Дополнительные возможности декорирования предоставляет модуль functools декоратор.

# Декоратор wraps
"""
def count(param):
    def deco(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            ...
            return result

        return wrapper

    return deco
"""
# ✔ __name__ получает имя декорируемой функции
# ✔ help() возвращает справку декорируемой функции


import time
from functools import wraps
from typing import Callable


def count(num: int = 1):
    def deco(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time_for_count = []
            result = None
            for _ in range(num):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                stop = time.perf_counter()
                time_for_count.append(stop - start)
            print(f'Результаты замеров {time_for_count}')
            return result

        return wrapper

    return deco


@count(3)
def factorial(n: int) -> int:
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


print(f'{factorial(1000) = }')
print(f'{factorial.__name__ = }')  # 'wrapper'
help(factorial)  # Help on function wrapper in module __main__:  wrapper(*args, **kwargs)

# Декоратор wraps добавляется к функции wrapper, т.е. к самой глубоко вложенной функции.
# В качестве аргумента wraps должен получить параметр декларируемой функции.
# Теперь factorial возвращает свои название и строку документации.

# выше дописали @wraps(func) и как итог:

print(f'{factorial.__name__ = }')  # 'factorial'
help(factorial)  # Help on function factorial in module __main__:  factorial(n: int) -> int
