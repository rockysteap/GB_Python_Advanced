# Чтение CSV в словарь

# csv_file = csv.DictReader(f, fieldnames=["name", "sex", "age", "height", "weight", "office"],
#                           restkey="new", restval="Main Office")

# Дополнительные параметры:
# ● fieldnames — список заголовков столбцов, ключей словаря
# ● restkey — значение ключа для столбцов, которых нет в fieldnames
# ● restval — значение поля для ключей fieldnames, которых нет в файле CSV


# Ключи словаря — названия столбцов, значения — очередная строка файла CSV.
# Прочитаем файл biostats_tab.csv из примера выше, но не в список, а в словарь

# Воспользуемся классом DictReader.
"""
import csv

with open('biostats_tab.csv', 'r', newline='') as f:
    csv_file = csv.DictReader(f, fieldnames=["name", "sex", "age", "height", "weight", "office"],
                              restkey="new", restval="Main Office", dialect='excel-tab',
                              quoting=csv.QUOTE_NONNUMERIC)
    for line in csv_file:
        print(f'{line = }')
        print(f'{line["name"] = }\t{line["age"] = }')

# line = {'name': 'Name', 'sex': 'Sex', 'age': 'Age', 'height': 'Height (in)', 'weight': 'Weight (lbs)',
#           'office': 'Main Office'}
# line["name"] = 'Name'	line["age"] = 'Age'
# line = {'name': 'Alex', 'sex': 'M', 'age': 41.0, 'height': 74.0, 'weight': 170.0, 'office': 'Main Office'}
# line["name"] = 'Alex'	line["age"] = 41.0
# ...
"""

# Если передать список строк в параметр fieldnames, они будут использоваться для ключей словаря,
# а не первая строка файла. В нашем примере передан “лишний” ключ count, т.к. в таблице нет шестого столбца,
# ему было присвоено значение из параметра restval.

import csv

with open('biostats_tab.csv', 'r', newline='') as f:
    csv_file = csv.DictReader(f, fieldnames=["name", "sex", "age", ], restkey="new", restval="Main Office",
                              dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
    for line in csv_file:
        print(f'{line = }')
        print(f'{line["name"] = }\t{line["age"] = }')

# line = {'name': 'Name', 'sex': 'Sex', 'age': 'Age', 'new': ['Height (in)', 'Weight (lbs)']}
# line["name"] = 'Name'	line["age"] = 'Age'
# line = {'name': 'Alex', 'sex': 'M', 'age': 41.0, 'new': [74.0, 170.0]}
# line["name"] = 'Alex'	line["age"] = 41.0
# ...

# Если количество ключей оказывается меньше, чем столбцов, недостающий ключ берётся из параметра restkey.
# При этом все столбцы без ключа сохраняются как элементы списка в restkey ключ.
