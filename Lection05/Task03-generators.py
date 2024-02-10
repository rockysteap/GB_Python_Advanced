# Важно! Генератор не обязан быть однострочником.
"""
a = range(0, 10, 2)
print(f'{a=}, {type(a)=}, {a.__sizeof__()=}, {len(a)}')
b = range(-1_000_000, 1_000_000, 2)
print(f'{b=}, {type(b)=}, {b.__sizeof__()=}, {len(b)}')
"""

# Генератор 'a' на пять значений и генератор 'b' на 1 млн. значений занимают одинаковое место в памяти.

# Генераторные выражения
# Генераторные выражения Python позволяют создать собственный генератор, перебирающий значения.
"""
my_gen = (chr(i) for i in range(97, 123))
print(my_gen)  # <generator object <genexpr> at 0x>
for char in my_gen:
    print(char)
"""

# Для создания генераторного выражения используют круглые скобки, внутри которых прописывается логика выражения.

# Комбинации for и if в генераторах и выражениях
"""
x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)
res = list(mult)
print(f'{len(res)=}\n{res}')
"""

# List comprehensions
"""
my_listcomp = [chr(i) for i in range(97, 123)]
print(my_listcomp)  # ['a', 'b', 'c', 'd', ..., z]
for char in my_listcomp:
    print(char)
"""

# Длинный код:
"""
data = [2, 5, 1, 42, 65, 76, 24, 77]
res = []
for item in data:
    if item % 2 == 0:
        res.append(item)
print(f'{res = }')  # res = [2, 42, 76, 24]
"""

# Аналогичное решение, но с использованием синтаксического сахара listcomp:
"""
data = [2, 5, 1, 42, 65, 76, 24, 77]
res = [item for item in data if item % 2 == 0]
print(f'{res = }')  # res = [2, 42, 76, 24]
"""

# Генераторные выражения или генерация списка
"""
x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
res = [i + j for i in x if i % 2 != 0 for j in y if j != 1]
print(f'{len(res)=}\n{res}')
"""
# Если нам не нужны все элементы разом. Например, мы в дальнейшем хотим перебирать значения по одному в цикле.
# В этом случае подойдет генераторное выражение без преобразования в список.
"""
x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)
for item in mult:
    print(f'{item = }')
"""
# 🔥 Важно! При написании кода заранее решите нужна вам сгенерированная коллекция целиком или нет.
# Не стоит тратить память на хранение всех элементов, если вы ими не пользуетесь одновременно.

# Set comprehensions
"""
my_setcomp = {chr(i) for i in range(97, 123)}
print(my_setcomp)  # {'f', 'g', 'b', 'j', 'e',... }
for char in my_setcomp:
    print(char)
"""

# Set comprehensions
# set_comp = {expression for expr in sequence1 if condition1 …}

# Dict comprehensions
# dict_comp = {key: value for expr in sequence1 if condition1 …}

# Сходства и различия
# {используются фигурные скобки для выражения}
# словарь подставляет ключ и значение через двоеточие


# Dict comprehensions
# Ещё один вариант синтаксического сахара — генерация словаря.
"""
my_dictcomp = {i: chr(i) for i in range(97, 123)}
print(my_dictcomp)  # {97: 'a', 98: 'b', 99: 'c',... }
for number, char in my_dictcomp.items():
    print(f'dict[{number}] = {char}')
"""

# 🔥 Важно! Стоит помнить, что ключи словаря должны быть объектами неизменяемого типа.

#  Функция-генератор
""" Обычная функция
def factorial(n):
    number = 1
    result = []
    for i in range(1, n + 1):
        number *= i
        result.append(number)
    return result


for i, num in enumerate(factorial(10), start=1):
    print(f'{i}! = {num}')
"""

# Команда yield превращает функцию в генератор.
# Значение после yield возвращается из функции.
# Сама функция запоминает своё состояние: строку, на которой остановилось выполнение, значения локальных переменных.
# Повторный вызов функции продолжает работу с момента остановки.
"""
def factorial(n):
    number = 1
    for i in range(1, n + 1):
        number *= i
        yield number

for i, num in enumerate(factorial(10), start=1):
    print(f'{i}! = {num}')

# Функции iter и next для генераторов
# iter и next могут работать с созданными генераторами:

my_iter = iter(factorial(4))
print(my_iter)
print(next(my_iter))  # 1
print(next(my_iter))  # 2
print(next(my_iter))  # 6
print(next(my_iter))  # 24
# print(next(my_iter))  # StopIteration (ERROR)
"""
