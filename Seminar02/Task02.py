import sys
from typing import Hashable

data = [1, 2., '3', [4], (5,)]
data.extend([1, 2., '3', [4], (5,)])

for n, obj in enumerate(data, 1):
    print(f'{n} {obj} {id(obj)} {sys.getsizeof(obj)} '
          f'{hash(obj) if isinstance(obj, Hashable) else "Объект нехэшируемый"} '
          f'{"Число целое" if isinstance(obj, int) else ""} '
          f'{"Строка" if isinstance(obj, str) else ""}')

