import pytest


# Кейсов всего два: test_first_num и test_first_chr.
# И каждый из них использует свои фикстуры.


# ➢ Фикстура get_file
# Фикстура принимает на вход аргумент tmp_path.
# Это встроенная фикстура, которая возвращает временный путь - объект pathlib.Path.
# При использовании выводим не печать информацию о создании файла и о его удалении.
# Отследим когда срабатывает фикстура.
@pytest.fixture
def get_file(tmp_path):
    f_name = tmp_path / 'test_file.txt'
    print(f'Создаю файл {f_name}')  # принт в учебных целях
    with open(f_name, 'w+', encoding='utf-8') as f:
        yield f
    print(f'Закрываю файл {f_name}')  # принт в учебных целях


# Внутри менеджера контекста создаём файл и через команду yield возвращаем указатель на него.
# Если бы мы использовали команду return, менеджер контекста вызвал бы f.close() после возврата указания
# и файл стал бы нечитаемым.
# Используя yield мы превратили функцию в генератор.
# Теперь внутри фикстуры есть “setUp” создающий файл и “tearDown”, закрывающий его после использования.

# Внимание!
# Мы явно не удаляем временные файлы.
# Фикстура tmp_path сохраняет три последних временных каталога, удаляя старые при очередном запуске.


# ➢ Фикстура set_num
# Используя файловый дескриптор get_file записываем строку из цифр и возвращаем указатель на начало файла.
# Фикстура ничего не возвращает.
@pytest.fixture
def set_num(get_file):
    print(f'Заполняю файл {get_file.name} цифрами')  # принт в учебных целях
    for i in range(10):
        get_file.write(f'{i:05}')
        get_file.seek(0)


# ➢ Фикстура set_char
# Снова используем файловый дескриптор get_file, но получаем уже другой файл.
# Имя совпадает, но каталоги разные.
# Заполняем его буквами, сбрасываем позицию в ноль и возвращаем get_file - файловый дескриптор.
@pytest.fixture
def set_char(get_file):
    print(f'Заполняю файл {get_file.name} буквами')  # принтим в чебных целях
    for i in range(65, 91):
        get_file.write(f'{chr(i)}')
    get_file.seek(0)
    return get_file


# ➢ Кейс test_first_num
# Перед началом теста срабатывают фикстуры, создающие временный файл и заполняющие его цифрами.
# Далее обращаемся к get_file, чтобы прочитать пять первых символов и сравниваем их со строкой текста.
def test_first_num(get_file, set_num):
    first = get_file.read(5)
    assert first == '00000'


# ➢ Кейс test_first_char
# Кейс получает всего одну фикстуру set_char.
# Но так как она самостоятельно вызывает фикстуру get_file и возвращает её,
# мы можем обращаться к файловому дескриптору по имени set_char.
def test_first_char(set_char):
    first = set_char.read(5)
    assert first == 'ABCD'  # специально провалим тест


if __name__ == '__main__':
    pytest.main(['-v'])