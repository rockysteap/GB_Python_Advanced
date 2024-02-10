# Замыкание функций с изменяемыми типами данных.

# У каждой из двух функций hello и bye оказывается свой список names.
# Они не связаны между собой, но каждый хранит список имён до конца работы программы.


from typing import Callable


def add_one_str(a: str) -> Callable[[str], str]:
    names = []

    def add_two_str(b: str) -> str:
        names.append(b)
        return a + ', ' + ', '.join(names)

    return add_two_str


hello = add_one_str('Hello')
bye = add_one_str('Goodbye')

print(hello('Alex'))  # Hello, Alex
print(hello('Karina'))  # Hello, Alex, Karina
print(bye('Alina'))  # Goodbye, Alina
print(hello('John'))  # Hello, Alex, Karina, John
print(bye('Neo'))  # Goodbye, Alina, Neo
