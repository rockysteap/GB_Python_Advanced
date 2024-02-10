# Замыкание (closure) — функция, которая находится внутри другой функции
# и ссылается на переменные объявленные в теле внешней функции (свободные переменные).

# Внутренняя функция создается каждый раз во время выполнения внешней.
# Каждый раз при вызове внешней функции происходит создание нового экземпляра внутренней функции,
# с новыми ссылками на переменные внешней функции.

from typing import Callable


def add_one_str(a: str) -> Callable[[str], str]:
    def add_two_str(b: str) -> str:
        return a + ' ' + b

    return add_two_str


hello = add_one_str('Hello')
bye = add_one_str('Goodbye')

print(hello('world!'))  # Hello world!
print(hello('friend!'))  # Hello friend!
print(bye('wonderful world!'))  # Goodbye wonderful world!

print(f'{type(add_one_str) = }, {add_one_str.__name__ = }, {id(add_one_str) = }')
# type(add_one_str) = <class 'function'>, add_one_str.__name__ = 'add_one_str', id(add_one_str) = 2336032773504

print(f'{type(hello) = }, {hello.__name__ = }, {id(hello) = }')
# type(hello) = <class 'function'>, hello.__name__ = 'add_two_str', id(hello) = 2336033046592

print(f'{type(bye) = }, {bye.__name__ = }, {id(bye) = }')
# type(bye) = <class 'function'>, bye.__name__ = 'add_two_str', id(bye) = 2336033775328


