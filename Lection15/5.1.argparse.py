# Модуль argparse

# Запуск скриптов с параметром.
# Модуль argparse по сути надстраивается над sys.argv.
# Он генерирует справку, определяет способ анализа аргументов командной строки,
# сообщает об ошибках и даёт подсказки.

import argparse

parser = argparse.ArgumentParser(description='My first argument parser')
parser.add_argument('numbers', metavar='N', type=float, nargs='*',
                    help='press some numbers')
args = parser.parse_args()
print(f'В скрипт передано: {args}')

# 💡 Внимание! Тут и далее до конца главы запускать файл будет из терминала ОС.
#       Примерно так:
#       $ python main.py ... , где многоточие - передаваемые скрипту аргументы

# Запустим скрипт с несколькими значениями:
# $ python3 main.py 42 3.14 73

# На выходе получаем объект Namespace(numbers=[42.0, 3.14, 73.0]).

# Как это работает?
# 1. Создаём объект парсер при помощи класса ArgumentParser с первоначальными настройками экземпляра.
# 2. Добавляем в полученный экземпляр аргументы для парсинга через метод add_argument.
#   Количество аргументов может быть любым. И каждый может содержать свои настройки.
# 3. Выгружаем результаты, переданные при запуске скрипта в терминале и обработанные парсером
#   в виде объекта Namespace. Для этого вызываем метод экземпляра parse_args.
#   Прежде чем разобрать каждый пунктов подробнее запустим скрипт ещё пару раз:
#   с ключом --help и с каким-нибудь текстом.


# (venv) PS E:\Coding\Projects\GB_Python_Advanced\Lection15> python.exe .\5.1.argparse.py 42 3.14 73 sd
# usage: 5.1.argparse.py [-h] [N ...]


# (venv) PS E:\Coding\Projects\GB_Python_Advanced\Lection15> python.exe .\5.1.argparse.py --help
# usage: 5.1.argparse.py [-h] [N ...]
#
# My first argument parser
#
# positional arguments:
#   N           press some numbers
#
# options:
#   -h, --help  show this help message and exit


# (venv) PS E:\Coding\Projects\GB_Python_Advanced\Lection15> python.exe .\5.1.argparse.py Hello world!
# usage: 5.1.argparse.py [-h] [N ...]
# 5.1.argparse.py: error: argument N: invalid float value: 'Hello'
