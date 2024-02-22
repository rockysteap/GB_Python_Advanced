# Перед вами несколько строк doctest.
# Напишите что должна делать программа, чтобы пройти тесты. У вас 3 минуты.

def say(text: str, mul: int = 2, sep: str = ' ') -> str:
    """
    >>> say('Hello')
    Hello Hello
    >>> say('Hi', 5)
    Hi Hi Hi Hi Hi
    >>> say('cat', 3, '(=^.^=)')
    cat(=^.^=)cat(=^.^=)cat
    """
    res = text
    for i in range(mul):
        if i > 0:
            res += sep
            res += text

    return res  # 0 passed and 3 failed.
    # print(res)  # 3 passed and 0 failed.


if __name__ == '__main__':
    # print(say('Hello'))
    # print(say('Hi', 5))
    # print(say('cat', 3, '(=^.^=)'))
    import doctest

    doctest.testmod(verbose=True)
