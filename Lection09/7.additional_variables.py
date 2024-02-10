# Дополнительные переменные в декораторе

# Мы уже замыкали внутри функции список для хранения переданных имён.
# Декораторы открывают большие возможности по модификации основной функции.
# Рассмотрим пример простого кэширующего декоратора.


# 🔥 Важно!
# Мы специально исключили параметр **kwargs из функции wrapper, т.к. это словарь ключевых аргументов.
# Попытка использования в качестве ключа словаря _cache_dict другого словаря kwargs приведёт к ошибке.
# Ключом может выступать только неизменяемые объекты.


from typing import Callable


def cache(func: Callable):
    _cache_dict = {}

    def wrapper(*args):
        if args not in _cache_dict:
            _cache_dict[args] = func(*args)
        return _cache_dict[args]

    return wrapper


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
