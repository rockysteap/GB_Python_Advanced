def string_parse(string: str) -> str:
    """
    Обрабатывает строку.
    :param string:
    :return:

    >>> string_parse('Строки нумеруются начиная с единицы.')
    '1     Строки\n2   единицы.\n3    начиная\n4 нумеруются\n5          с\n'
    """
    data = string.split()
    data.sort()

    longest_word = len(max(data, key=len))

    res = ''
    for n, s in enumerate(data, 1):
        res += f'{n} {s:>{longest_word}}\n'

    return res


s = 'Строки нумеруются начиная с единицы.'
print(string_parse(s))
# help(string_parse)
