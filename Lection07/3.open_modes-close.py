"""
f = open('text_data.txt', 'a', encoding='utf-8')
f.write('Окончание файла\n')
# (a)ppend -> добавляет в конец файла
f.close()
"""

"""
f = open('bin_data', 'wb', buffering=64)
f.write(b'X' * 1200)
f.close()
"""

# 'buffering' — определяет режим буферизации.
# При работе с бинарными файлами можно передать 0 — отключить буферизацию.
# В текстовом режиме можно передать 1 — использовать буферизацию строк.
# Число больше единицы определяет размер буфера в байтах для двоичных файлов.
# По умолчанию размер буфера подстраивается под файловую систему и обычно равен 4096 или 8192 байта.

# errors — используется только в текстовом режиме и определяет поведение в случае
# ошибок кодирования или декодирования.

# Рассмотрим несколько возможных вариантов параметра:

# ➢ 'strict' — вызывает исключение ValueError в случае ошибки.
#       Работает как значение по умолчанию.
# ➢ 'ignore' — игнорирует ошибки кодирования.
#       При этом игнорирование ошибок может привести к потере данных.
# ➢ 'replace' — вставляет маркер замены (например, '?') там, где есть некодируемые данные.
# ➢ 'namereplace' — при записи заменяет неподдерживаемые символы последовательностями \N{...}.
# ➢ 'newline' — отвечает за преобразование окончания строки
# ➢ 'closefd' — указывает оставлять ли файловый дескриптор открытым при закрытии файла
# ➢ 'opener' — позволяет передать пользовательскую функцию для открытия файла.

"""
f = open('data.txt', 'wb')
f.write('Привет, '.encode('utf-8') + 'мир!'.encode('cp1251'))
f.close()

# f = open('data.txt', 'r', encoding='utf-8')
# print(list(f))  # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xec in position 14: invalid continuation byte
# f.close()

f = open('data.txt', 'r', encoding='utf-8', errors='replace')
print(list(f))
f.close()
"""