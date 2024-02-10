def max_before_hundred(*args):
    """Return the maximum number not exceeding 100."""
    m = float('-inf')
    for item in args:
        if m < item < 100:
            m = item
    return m


print(max_before_hundred(-42, 73, 256, 0))


# 🔥 Внимание! В программе использована переменная, а точнее константа
# “минус бесконечность” float('-inf'). Это особая форма представления
# бесконечности в памяти интерпретатора, аналогичная бесконечности из модуля my_math.


def max_before_hundred(*args):
    """Return the maximum number not exceeding 100.
    :param args: tuple of int or float numbers
    :return: int or float number from the tuple args
    """
    pass


help(max_before_hundred)
