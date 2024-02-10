from random import randint

# Явно указать какие объекты нужно импортировать при использовании from module import *
# можно через магическую переменную __all__

__all__ = ['func', '_secret']

SIZE = 100
_secret = 'qwerty'
__top_secret = '1q2w3e4r5t6y'


def func(a: int, b: int) -> str:
    z = f'В диапазоне от {a} до {b} получили {randint(a, b)}'
    return z


result = func(1, 6)
