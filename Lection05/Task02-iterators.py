# 💡 Секрет! На самом деле порядок вывода элементов множества не случаен.
# Он зависит от результата работы встроенного хэша.
# Хэш функция определяет в какое место множества будет помещён элемент и возвращает их в порядке возрастания хеша.

# ● Функция iter
# Функция iter имеет формат iter(object[, sentinel]).
# object является обязательным аргументом.
# Если объект не реализует интерфейс итерации через методы __iter__ или __getitem__, получим ошибку TypeError.
"""
a = 42
iter(a) # TypeError: 'int' object is not iterable
"""

"""
data = [2, 4, 6, 8]
list_iter = iter(data)
print(list_iter)  # <list_iterator object at 0x0000024F486417B0>

data = [2, 4, 6, 8]
list_iter = iter(data)
print(*list_iter)  # 2 4 6 8
print(*list_iter)
"""
# 🔥 Внимание! Обратите внимание, что итератор является одноразовым объектом.
# Получив все элементы коллекции один раз он перестаёт работать.
# Для повторного извлечения элементов необходимо создать новый итератор.
"""
data = [2, 4, 6, 8]
# list_iter = iter(data, 6) # TypeError: iter(v, w): v must be callable

import functools
f = open('mydata.bin', 'rb')
for block in iter(functools.partial(f.read, 16), b''):
    print(block)
f.close()
"""

# ● Функция next

# Функция next имеет формат next(iterator[, default]).
# На вход функция принимает итератор, который вернула функция iter.
# Каждый вызов функции возвращает очередной элемент итератора.
"""
data = [2, 4, 6, 8]
list_iter = iter(data)
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))  # StopIteration (ERROR)
"""


data = [2, 4, 6, 8]
list_iter = iter(data)
print(next(list_iter, 42))  # 2
print(next(list_iter, 42))  # 4
print(next(list_iter, 42))  # 6
print(next(list_iter, 42))  # 8
print(next(list_iter, 42))  # 42 <- выводится переданное значение по умолчанию
print(next(list_iter, 42))  # 42 <- выводится переданное значение по умолчанию


data = {"один": 1, "два": 2, "три": 3}
x = iter(data.items())
print(x)
y = next(x)
print(y)
z = next(iter(y))
print(z)
