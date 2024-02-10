# ● Текущий каталог

# Для получения информации о текущем каталоге можно использовать модуль os или pathlib

import os
from pathlib import Path

# pathlib более современная библиотека, чем os

# cwd -> current work directory
print(os.getcwd())  # E:\Coding\Projects\GB_Python_Advanced\Lection07

# cwd -> current work directory
print(Path.cwd())  # E:\Coding\Projects\GB_Python_Advanced\Lection07

print(os.getcwd())
print(Path.cwd())

os.chdir('../..')
# Перешли на две папки выше

print(os.getcwd())
print(Path.cwd())

# создание директорий
"""
os.mkdir('new_os_dir')  # если повторно -> FileExistsError:
# [WinError 183] Невозможно создать файл, так как он уже существует: 'new_os_dir'
Path('new_path_dir').mkdir()
"""

# Представленный код создаёт каталог в текущей директории. А если необходимо
# создать несколько вложенных друг в друга каталогов, код будет следующим:
"""
os.makedirs('dir/other_dir/new_os_dir')
Path('some_dir/dir/new_path_dir').mkdir()  # FileNotFoundError
Path('some_dir/dir/new_path_dir').mkdir(parents=True)
"""

# ● Удаление каталогов

# Для удаления одного каталога подойдут следующие функция и метод

# os.rmdir('dir') # OSError
# Path('some_dir').rmdir() # OSError
os.rmdir('dir/other_dir/new_os_dir')
Path('some_dir/dir/new_path_dir').rmdir()

# Обратите внимание, что при передаче цепочки каталогов удаляется один, последний из перечисленных.
# Родительские каталоги остаются без изменений.
