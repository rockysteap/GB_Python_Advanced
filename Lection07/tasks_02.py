import os
import shutil
from pathlib import Path

# Создает в текущем каталоге 10 файлов с именами file_0.txt -> file_9.txt и помещает в них строку 'Hello world!'
for i in range(10):
    with open(f'file_{i}.txt', 'w', encoding='utf-8') as f:
        f.write('Hello world!')

# Создает в текущем каталоге папку new_dir
os.mkdir('new_dir')

# Для i = 2, 4, 6, 8
for i in range(2, 10, 2):
    # сохраняет путь к файлу в переменную f
    f = Path(f'file_{i}.txt')
    # перемещает файл в папку new_dir
    f.replace('new_dir' / f)

# Копирует содержимое папки new_dir в новую папку dir_new, при этом создавая её
shutil.copytree('new_dir', Path.cwd() / 'dir_new')
