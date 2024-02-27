# Напишите программу, которая использует модуль logging для вывода сообщения об ошибке в файл.
# Например, отлавливаем ошибку деления на ноль.

import logging

logging.basicConfig(filename='task01.log', encoding='utf-8', level=logging.NOTSET)


def division(x: int | float, y: int | float):
    try:
        res = x / y
        logging.debug(f"x / y = {res}")
        return res
    except ZeroDivisionError as err:
        logging.error(f'{err}: На ноль делить нельзя')


if __name__ == '__main__':
    division(3, 0)
    division(3, 5)
    division(3, 1)
