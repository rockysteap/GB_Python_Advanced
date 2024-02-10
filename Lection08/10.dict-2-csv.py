# Запись CSV из словаря

# ● Параметры класса DictWriter аналогичны параметрам DictReader

# ● csv_write.writeheader()
#       сохранение первой строки с заголовками в порядке их перечисления в параметре fieldnames
# ● csv_write.writerow(line)
#       сохранение списка в одной строке файла в формате CSV
# ● csv_write.writerows(all_data)
#       сохранение матрицы в нескольких строках файла в формате CSV

"""
"""
import csv

with (
    open('biostats_tab.csv', 'r', newline='') as f_read,
    open('biostats_new.csv', 'w', newline='', encoding='utf-8') as f_write
):
    csv_read = csv.DictReader(f_read, fieldnames=["name", "sex", "age", "height", "weight", "office"],
                              restval="Main Office", dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
    csv_write = csv.DictWriter(f_write, fieldnames=["id", "name", "office", "sex", "age", "height", "weight"],
                               dialect='excel-tab', quoting=csv.QUOTE_ALL)
    csv_write.writeheader()
    all_data = []
    for i, dict_row in enumerate(csv_read):
        if i != 0:
            dict_row['id'] = i
            dict_row['age'] += 1
            all_data.append(dict_row)
    csv_write.writerows(all_data)


# В файле записано следующее:
# "id"	"name"	"office"	"sex"	"age"	"height"	"weight"
# "1"	"Alex"	"Main Office"	"M"	"42.0"	"74.0"	"170.0"
# "2"	"Bert"	"Main Office"	"M"	"43.0"	"68.0"	"166.0"
# ...

# Класс DictWriter получил список полей для записи, где добавлено новое поле id.
# В качестве диалекта выбран excel с табуляцией.
# В параметре quoting указали, что все значения стоит заключать в кавычки.
# Новый для нас метод writeheader сохранил первую строку с заголовками в том порядке,
#   в котором мы их перечислили в параметре fieldnames.
# Далее мы работаем с элементами словаря и формируем список словарей для одноразовой записи в файл.
