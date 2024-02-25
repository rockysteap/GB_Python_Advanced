# Обратные методы, позволяющие создать объекты datetime.
from datetime import datetime

date_original = '2022-12-12 18:01:21.555470'
original_date = datetime.fromisoformat(date_original)

date_timestamp = 1181862840.000024
timestamp_date = datetime.fromtimestamp(date_timestamp)

date_iso = '2007-06-15T02:14:00.000024'
iso_date = datetime.fromisoformat(date_iso)

date_text = 'Дата 15 June 2007. День недели Friday. Время 02:14:00. Это 24 неделя и 166 день года.'
text_date = datetime.strptime(date_text, 'Дата %d %B %Y. День недели %A. Время %H:%M:%S. Это %W неделя и %j день года.')

print(original_date)  # 2022-12-12 18:01:21.555470
print(timestamp_date)  # 2007-06-15 02:14:00.000024
print(iso_date)  # 2007-06-15 02:14:00.000024
print(text_date)  # 2007-06-15 02:14:00

# ● fromisoformat — метод анализирует строку текст и если она совпадает со стандартом ISO 8601,
#       возвращает объект datetime.
#   Стандартный вывод объектов на печать позволяет делать обратное преобразование этим методом.

# ● fromtimestamp — получаем объект даты из целого или вещественного числа.
#   Само число — количество секунд после полуночи 1 января 1970.

# ● strptime — метод принимает на вход два параметра:
#   строку для преобразования и строку с форматом.
#   Если формат позволяет проанализировать строку, возвращается объект datetime.
