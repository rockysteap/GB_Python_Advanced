# 🔥 Внимание!
# Вдохновение JUnit сказалось на стиле фреймворка,
# а именно на использовании camelCase для имён,
# вместо привычного для Python разработчика стиля snake_case.

import unittest


class TestCaseName(unittest.TestCase):
    def test_method(self):
        self.assertEqual(2 * 2, 5, msg='Видимо и в этой вселенной не работает :-(')


if __name__ == '__main__':
    unittest.main()

# 🔥 Внимание!
# Команда для запуска тестов из командной строки выглядит аналогично запуску doctest
# $ python3 -m unittest tests.py -v
