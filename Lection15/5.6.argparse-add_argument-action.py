import argparse

parser = argparse.ArgumentParser(description='Sample')
parser.add_argument('-x', action='store_const', const=42)
parser.add_argument('-y', action='store_true')
parser.add_argument('-z', action='append')
parser.add_argument('-i', action='append_const', const=int, dest='types')
parser.add_argument('-f', action='append_const', const=float, dest='types')
parser.add_argument('-s', action='append_const', const=str, dest='types')
args = parser.parse_args()

print(args)
# (venv) PS E:\Coding\Projects\GB_Python_Advanced\Lection15>
#                           python .\5.6.argparse-add_argument-action.py -x -y -z 42 -z 73 -i -f -s
# Namespace(x=42, y=True, z=['42', '73'], types=[<class 'int'>, <class 'float'>, <class 'str'>])

# https://docs.python.org/3.10/library/argparse.html#action

# Параметр action принимает одно из определённых строковых значений и срабатывает
# при наличии в строке вызова скрипта соответствующего параметра.
#   ● store_const — передаёт в args ключ со значением из параметра const
#   ● store_true или store_false — сохраняет в ключе истину или ложь
#   ● append — ищет несколько появлений ключа и собирает все значения после него в список
#   ● append_const — добавляет значение из ключа в список, если ключ вызван.

#   ○ параметр dest переопределяет имя ключа в Namespace на своё.

# В результате несколько разных ключей при вызове скрипта имеют одно имя при оценке результата.

# (venv) PS E:\Coding\Projects\GB_Python_Advanced\Lection15> python .\5.6.argparse-add_argument-action.py -h
# usage: 5.6.argparse-add_argument-action.py [-h] [-x] [-y] [-z Z] [-i] [-f] [-s]

# Sample

# options:
#   -h, --help  show this help message and exit
#   -x
#   -y
#   -z Z
#   -i
#   -f
#   -s
