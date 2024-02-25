from datetime import datetime

dt = datetime(year=2007, month=6, day=15, hour=2, minute=14, microsecond=24)

print(dt)
# 2007-06-15 02:14:00.000024
print(dt.timestamp())
# 1181862840.000024
print(dt.isoformat())
# 2007-06-15T02:14:00.000024
print(dt.weekday())
# 4  # <- пятница (дни недели от 0 (пон) до 6 (вос))
print(dt.strftime('Дата %d %B %Y. День недели %A. Время %H:%M:%S. Это %W неделя и %j день года.'))
# Дата 15 June 2007. День недели Friday. Время 02:14:00. Это 24 неделя и 166 день года.

# ● timestamp — возвращаем время в секундах от начала времён.
#   Под началом времён понимаем POSIX-время, т.е полночь 1 января 1970 года.
#   Программисты использует его как особую точку отсчёта, позволяющую хранить время как целое
#   (если нужна точность до секунды) или вещественное число.
#   Подобный подход используется для хранения времени в БД и для манипуляций со временем.

# ● isoformat — выводит дату в формате, соответствующем стандарту ISO 8601.
#   Это международный стандарт описывающий формат даты и времени и рекомендации по его использованию.

# ● weekday — позволяет получить день недели в виде целого числа, где 0 - понедельник, а 6 — воскресенье.

# ● strftime — выводит дату в соответствии с переданным в виде str форматом.

# Обычный текст выводится без изменения, а символ % указывает на следующий после него литер форматирования.
#   Ознакомится со всеми можно по ссылке
#   https://docs.python.org/3.10/library/datetime.html#strftime-and-strptime-behavior.
