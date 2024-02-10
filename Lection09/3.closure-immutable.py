# Замыкание функций с неизменяемыми типами данных.

# Что более важно - неизменяемый тип данных у строки text.
# Без добавления строчки кода nonlocal text была бы получена ошибка
# UnboundLocalError: local variable 'text' referenced before assignment.

# Мы явно указали, что хотим обращаться к неизменяемому объекту для изменения его значения.

from typing import Callable


def add_one_str(a: str) -> Callable[[str], str]:
    text = ''

    def add_two_str(b: str) -> str:
        nonlocal text
        text += ', ' + b
        return a + text

    return add_two_str


hello = add_one_str('Hello')
bye = add_one_str('Good bye')

print(hello('Alex'))
print(hello('Karina'))
print(bye('Alina'))
print(hello('John'))
print(bye('Neo'))
