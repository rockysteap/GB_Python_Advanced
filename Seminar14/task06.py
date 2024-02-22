# Задание №6.
# На семинаре 13 был создан проект по работе с
# пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.

import pytest

from Seminar14.rect import Rectangle


@pytest.fixture
def r1():
    return Rectangle(4, 8)


@pytest.fixture
def r2():
    return Rectangle(2, 4)


def test_init_rectangle():
    assert Rectangle(4, 8) is not None, 'Error'


def test_init_rectangle_incorrect():
    with pytest.raises(ValueError):
        Rectangle(-3, 5)


def test_is_area_int(r1):
    assert isinstance(r1.area(), int)


def test_add_is_rectangle(r1, r2):
    assert isinstance(r1 + r2, Rectangle)


if __name__ == '__main__':
    pytest.main(['-vv'])
