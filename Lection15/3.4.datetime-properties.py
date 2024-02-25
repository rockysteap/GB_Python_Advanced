# Каждый из объектов позволяет прочитать хранимые свойства
# обратившись к ним по имени через точечную нотацию.

from datetime import time, date, datetime, timedelta

d = date(year=2007, month=6, day=15)
t = time(hour=2, minute=14, microsecond=24)
dt = datetime(year=2007, month=6, day=15, hour=2, minute=14, microsecond=24)

delta = timedelta(weeks=53, hours=73, minutes=101, seconds=303, milliseconds=60)

print(f'{d.month}')  # 6
print(f'{t.second}')  # 0
print(f'{dt.hour}')  # 2
print(f'{delta.days}')  # 374

# Даже если свойство явно не передано, но объект хранит его, мы можем получить доступ на чтение.

# Изменить значение напрямую не получится.
# Всё же перед нами неизменяемые объекты.
# Но мы можем воспользоваться методом replace для создания копии со значениями текущего объекта.
# Изменения затронут только указанные параметры.

# 💡 Внимание! timedelta не имеет метода replace.

# from datetime import time, date, datetime, timedelta

t = time(hour=2, minute=14, microsecond=24)
dt = datetime(year=2007, month=6, day=15, hour=2, minute=14, microsecond=24)
new_dt = dt.replace(year=2012)
one_more_hour = t.replace(t.hour + 1)

print(f'{new_dt}\n{one_more_hour}')
# 2012-06-15 02:14:00.000024
# 03:14:00.000024
