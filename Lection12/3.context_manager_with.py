# Менеджер контекста with запускает два дандер метода.
# Один в момент вызова менеджера, а второй в момент выхода из внутреннего блока кода.

# ● __enter__ — действия при входе в менеджер контекста
# ● __exit__ — действия при выходе из менеджера контекста

# Знакомая нам функция open() поддерживает работу с менеджером контекста.
# При вызове менеджера функция возвращает файловый дескриптор.
# А при выходе из него закрывает файл.

# Подобный функционал можно реализовать для любого объекта,
# где нужны одинаковые действия в начале и в конце.

# -----------------------------------------------
# Рассмотрим пример работы с базой данных sqlite.

# Получение
#   соединения с базой данных и получение
#   курсора из соединения — обязательное начало для работы с базой.

# Подтверждение изменений вызовом commit() и закрытие соединения с базой —
#   обязательные действия в конце работы с базой.
"""
import sqlite3
connection = sqlite3.connect('sqlite.db')
cursor = connection.cursor()
cursor.execute(\"""create table if not exists users(name, age);\""")
cursor.execute(\"""insert into users values ('Гвидо', 66);\""")
connection.commit()
connection.close()
"""

# Можно держать соединение открытым и подтверждать (коммитить) изменения после каждого действия с базой.
# А можно создать менеджер контекста.

import sqlite3


class DB:
    def __init__(self, name):
        self.name = name
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()
        self.cursor = self.connection = None


db = DB('sqlite.db')
with db as cur:  # AttributeError: __exit__ -> добавим выход __exit__
    cur.execute("""create table if not exists users(name, age);""")
    cur.execute("""insert into users values ('Гвидо', 66);""")
