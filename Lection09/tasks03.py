from random import randint
from typing import Callable


def count(num: int = 1):
    def deco(func: Callable):
        counter = []

        def wrapper(*args, **kwargs):
            for _ in range(num):
                result = func(*args, **kwargs)
                counter.append(result)
            return counter

        return wrapper

    return deco


@count(10)
def rnd(a: int, b: int) -> int:
    return randint(a, b)


print(f'{rnd(1, 10) = }')
print(f'{rnd(1, 100) = }')
print(f'{rnd(1, 1000) = }')

# rnd(1, 10) = [6, 5, 1, 8, 8, 4, 5, 1, 3, 3]
# rnd(1, 100) = [6, 5, 1, 8, 8, 4, 5, 1, 3, 3, 87, 67, 66, 43, 46, 66, 68, 56, 4, 64]
# rnd(1, 1000) = [6, 5, 1, 8, 8, 4, 5, 1, 3, 3, 87, 67, 66, 43, 46, 66, 68, 56, 4, 64, 151, 873, 816, 805, 251, 393,
#                   542, 848, 762, 210]
