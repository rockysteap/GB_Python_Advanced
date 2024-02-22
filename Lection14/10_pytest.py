# Финальный модуль для создания тестов — pytest.
# Он не входит в стандартную библиотеку Python, поэтому должен быть установлен перед использованием.

# pip install pytest

# 🔥 Важно! Версия Python должна быть 3.7 или выше.

# Команда assert

# В Python есть зарезервированное слово assert - утверждение.
# Если оно возвращает истину, программа продолжает работать.
# А если утверждение ложно, поднимается ошибка AssertionError.

# Для простоты можно представить assert как особую конструкцию if.

# ● “assert”
# assert утверждение, "Утверждение не подтвердилось"

# ● “if”
# if утверждение:
#   pass
# else:
#   raise AssertionError("Утверждение не подтвердилось")

import pytest


def sum_two_num(a, b):
    return a + b
    # return f'{a}{b}'


def test_sum():
    assert sum_two_num(2, 3) == 5, 'Математика покинула чат'


if __name__ == '__main__':
    pytest.main()


# Запуск pytest из командной строки:
#     pytest --doctest-modules prime.py -v
