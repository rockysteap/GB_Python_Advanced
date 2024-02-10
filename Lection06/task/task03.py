# 🔥 Важно! Генераторы псевдослучайных чисел модуля не должны
# использоваться в целях безопасности. Для обеспечения безопасности или
# криптографии необходимо использовать модуль secrets.

import random as rnd

print(f'{rnd.random()=}')
rnd.seed(42)
state = rnd.getstate()
print(f'{state=}')
print(f'{rnd.random()}')
print(f'{rnd.random()}')
rnd.setstate(state)
print(f'{rnd.random()}')
print(f'{rnd.random()}')
