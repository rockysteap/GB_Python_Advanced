def func(a, b, c):
    if a < b < c:
        raise ValueError('Не перемешано!')
    elif sum((a, b, c)) == 42:
        raise NameError('Это имя занято!')
    elif max(a, b, c, key=len) < 5:
        raise MemoryError('Слишком глуп!')
    else:
        raise RuntimeError('Что-то не так!!!')

# func(11, 7, 3)  # 1  # TypeError: object of type 'int' has no len()
# func(3, 2, 3)  # 2  # TypeError: object of type 'int' has no len()
# func(73, -40, 9)  # 3  # NameError: Это имя занято!
# func(10, 20, 30)  # 4  # ValueError: Не перемешано!
