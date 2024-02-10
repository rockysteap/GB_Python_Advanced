import os
from string import ascii_lowercase
from random import choice, randint

VOWELS = 'a', 'o', 'e', 'i', 'u', 'y'
LETTERS = ascii_lowercase


def create_files_ext(ext, min_name_len=6, max_name_len=30, min_bytes=256, max_bytes=4096, num_files=42):
    for _ in range(num_files):
        file_name = generate_pseudonyms(min_name_len, max_name_len) + ext
        file_size = randint(min_bytes, max_bytes)
        byte_list = bytes(randint(0, 255) for _ in range(file_size))
        with open(file_name, 'wb') as f:
            f.write(byte_list)
        print(f"Создан файл {file_name} размером {os.path.getsize(file_name)} байт")


def generate_pseudonyms(min_len=3, max_len=6) -> str:
    name = choice(VOWELS).upper() + ''.join(choice(LETTERS) for _ in range(randint(min_len, max_len)))
    return name


if __name__ == '__main__':
    create_files_ext(".txt", num_files=3)
