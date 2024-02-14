# Неизменяемые экземпляры, хеширование, __hash__

# Как вы помните ключом dict и элементами set и frozenset могут быть только неизменяемые типы данных.
# А для проверки на неизменяемость используется функция hash().
# Она должна возвращать целое число в 4 или 8 байт в зависимости от разрядности интерпретатора Python.
# И это число должно быть неизменным на всём протяжении работы программы.
# Попробуем сложить наши треугольники из примера выше в множество не изменяя код.
"""
from math import sqrt
class Triangle:
...
triangle_set = {Triangle(3, 4, 5), Triangle(6, 2, 5), Triangle(4, 4, 4), Triangle(3, 5, 3)}
print(triangle_set)
"""
# Получаем ошибку TypeError: unhashable type: 'Triangle' ведь дандер __hash__ у нас не реализован.
# Прежде чем приступать к написанию кода попробуем закомментировать метод проверки на равенство
# и запустит код снова.
"""
from math import sqrt
class Triangle:
...
def __eq__(self, other):
first = sorted((self.a, self.b, self.c))
second = sorted((other.a, other.b, other.c))
return first == second
...
triangle_set = {Triangle(3, 4, 5), Triangle(6, 2, 5), Triangle(4, 4, 4), Triangle(3, 5, 3)}
print(triangle_set)
print(', '.join(f'{hash(item)}' for item in triangle_set))
"""
# Работает! Экземпляры треугольника стали хэшируемыми. Правило следующее.
# ● нет __eq__, нет __hash__ - неизменяемый объект.
#                               Python сам реализует оба дандера
# ● есть __eq__, нет __hash__ - изменяемый объект.
#                               Python устанавливает __hash__ = None
# ● есть __eq__, есть __hash__ - неизменяемый объект реализованный разработчиком
# ● нет __eq__, есть __hash__ - запрещённая комбинация! Разработчик допустил ошибку

# Если вы хотите явно отключить поддержку хэширования,
# в определение класса добавляется строка __hash__ = None
# class Triangle:
# __hash__ = None
# ...

from math import sqrt


class Triangle:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def __str__(self):
        return f'Треугольник со сторонами: {self._a}, {self._b}, {self._c}'

    def __repr__(self):
        return f'Triangle({self._a}, {self._b}, {self._c})'

    def __eq__(self, other):
        first = sorted((self._a, self._b, self._c))
        second = sorted((other._a, other._b, other._c))
        return first == second

    def area(self):
        p = (self._a + self._b + self._c) / 2
        _area = (p * (p - self._a) * (p - self._b) * (p - self._c)) ** .5
        return _area

    def __lt__(self, other):
        return self.area() < other.area()

    def __hash__(self):
        return hash((self._a, self._b, self._c))


triangle_set = {Triangle(3, 4, 5), Triangle(6, 2, 5), Triangle(4,
                                                               4, 4), Triangle(3, 5, 3)}
print(triangle_set)
print(', '.join(f'{hash(item)}' for item in triangle_set))
