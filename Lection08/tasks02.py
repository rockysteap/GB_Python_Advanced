import csv

with open('quest.csv', 'w', newline='', encoding='utf-8') as f_write:
    csv_write = csv.DictWriter(f_write, fieldnames=["number", "name", "data"], restval='Hello world!', dialect='excel',
                               delimiter='#', quotechar='=', quoting=csv.QUOTE_NONNUMERIC)
    csv_write.writeheader()
    dict_row = {}
    for i in range(10):
        dict_row['number'] = i
        dict_row['name'] = str(i)
        csv_write.writerow(dict_row)


# Вывод в файл:
# =number=#=name=#=data=
# 0#=0=#=Hello world!=
# 1#=1=#=Hello world!=
# 2#=2=#=Hello world!=
# 3#=3=#=Hello world!=
# 4#=4=#=Hello world!=
# 5#=5=#=Hello world!=
# 6#=6=#=Hello world!=
# 7#=7=#=Hello world!=
# 8#=8=#=Hello world!=
# 9#=9=#=Hello world!=
