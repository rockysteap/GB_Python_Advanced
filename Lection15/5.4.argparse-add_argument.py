import argparse


def quadratic_equations(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    if d == 0:
        return -b / (2 * a)
    return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solving quadratic equations')
    parser.add_argument('param', metavar='a b c', type=float,
                        nargs=3, help='enter a b c separated by a space')
    args = parser.parse_args()
    print(quadratic_equations(*args.param))

# Первая строка превращается в имя свойства.
# Если она начинается с одиночного или двойного дефиса, параметр считается необязательным.
# Далее:
#   ● metavar — имя, которое выводится в справке
#   ● type — тип, для преобразования аргумента. Тип помогает контролировать передачу нужных значений.
#   ● nargs — указывает на количество значений, которые надо собрать из командной строки
#   и собрать результат в список list. Целое число указывает количество.
#   Кроме этого можно передать символ
#       “?” — один аргумент,
#       “*” — все имеющиеся аргументы,
#       “+” — все имеющиеся аргументы,
#       но не пустое# значение.
#   ● help - вывод подсказки об аргументе.

# (venv) PS E:\Coding\Projects\GB_Python_Advanced\Lection15> python .\5.4.argparse-add_argument.py -h
# usage: 5.4.argparse-add_argument.py [-h] a b c a b c a b c
# Solving quadratic equations
# positional arguments:
#   a b c       enter a b c separated by a space
#   -h, --help  show this help message and exit

# (venv) PS E:\Coding\Projects\GB_Python_Advanced\Lection15> python .\5.4.argparse-add_argument.py 2 -12 10
# (5.0, 1.0)
