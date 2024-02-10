#  Нерекомендуемый импорт через *
# from sys import *

import sys
# import random

# from sys import path as p
import random as rnd

from super_module import *

print(sys)
print(sys.builtin_module_names)
print(*sys.path, sep='\n')

# print(random.randint(1, 10))
print(rnd.randint(1, 10))

SIZE = 49.5
# print(f'{SIZE=}\n{result=}')  # не работает после использования __all__ внутри super_module
# print(f'{z = }')  # NameError: name 'z' is not defined
# print(f'{_secret = }')  # NameError: name '_secret' is not defined
print(f'{func(100, 200)=}\n{ rnd.randint(10, 20) = }')


def func(a: int, b: int) -> int:
    return a + b


print(f'{func(100, 200) = }')
