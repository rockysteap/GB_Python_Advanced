# Разработка через тестирование (англ. test-driven development, TDD) —
#   техника разработки программного обеспечения,
#   которая основывается на повторении очень коротких циклов разработки:
#       сначала пишется тест, покрывающий желаемое изменение,
#       затем пишется код, который позволит пройти тест,
#       и под конец проводится рефакторинг нового кода к соответствующим стандартам.
#
# В TDD выделяют следующие этапы:
#   1. Добавление теста
#   2. Запуск всех тестов: убедиться, что новые тесты не проходят
#   3. Написать код
#   4. Запуск всех тестов: убедиться, что все тесты проходят
#   5. Рефакторинг
#   6. Повторить цикл

def is_prime(p: int) -> bool:
    """
    Checks the number P for simplicity using finding the
    remainder of the division in the range [2, P).
    >>> is_prime(42)
    False
    >>> is_prime(73)
    True
    >>> is_prime(3.14)
    Traceback (most recent call last):
    ...
    TypeError: The number P must be an integer type
    >>> is_prime(-100)
    Traceback (most recent call last):
    ...
    ValueError: The number P must be greater than 1
    >>> is_prime(1)
    Traceback (most recent call last):
    ...
    ValueError: The number P must be greater than 1
    >>> is_prime(100_000_001)
    If the number P is prime, the check may take a long time.
    Working...
    False
    >>> is_prime(100_000_007)
    If the number P is prime, the check may take a long time.
    Working...
    True
    """
    if not isinstance(p, int):
        raise TypeError('The number P must be an integer type')
    elif p < 2:
        raise ValueError('The number P must be greater than 1')
    elif p > 100_000_000:
        print(f'If the number P is prime, the check may take a long time.\n'
              f'Working...')
    for i in range(2, p):
        if p % i == 0:
            return False
    return True


if __name__ == '__main__':
    import doctest

    # doctest.testmod(verbose=True)
    doctest.testfile('prime.md', verbose=True)

# Обратите внимание на многоточия в тестах ошибок.
# Модуль doctest ориентируется на первую строку об ошибке.
# Это или Traceback (most recent call last): или Traceback (innermost last):
# Так как номера строк кода, пути имена могут меняться, середина вывода игнорируется.
# Её можно заменить на многоточие.
# Важна последняя строка, которая начинается с типа ошибки и последующего за ней текста.


# 🔥 Важно!
# Так как doctest сравнивает текст, вызов ошибки,
# например через raise и печать аналогичного текста через print()
# будут восприниматься одинаково.
