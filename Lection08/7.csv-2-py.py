# Чтение CSV

# 🔥 Важно!
# При работе с CSV необходимо указывать параметр newline=’’ во время открытия файла.

# import csv

# with open('biostats.csv', 'r', newline='') as f:
                                # параметр newline='' для работы с CSV
    # csv_file = csv.reader(f)
                                # csv_file позволяет построчно читать csv файл в список list
"""
import csv

with open('biostats.csv', 'r', newline='') as f:
    csv_file = csv.reader(f)
    for line in csv_file:
        print(line)  # type(line) ->  < class 'list' >

# ['Name', 'Sex', 'Age', 'Height (in)', 'Weight (lbs)']
# ['Alex', 'M', '41', '74', '170']
# ['Bert', 'M', '42', '68', '166']
# ...
"""

"""
"""
import csv

with open('biostats_tab.csv', 'r', newline='') as f:
    csv_file = csv.reader(f, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
    for line in csv_file:
        print(line)

# ➢ dialect='excel-tab' — указали диалект с табуляцией в качестве разделителя
# ➢ quoting=csv.QUOTE_NONNUMERIC — передали встроенную константу, указывающую функции,
#       что числа без кавычек необходимо преобразовать к типу float.
