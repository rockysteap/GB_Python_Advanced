__all__ = ['parse_data']

__MONTHS = {
    1: range(1, 32),
    2: range(1, 29),
    3: range(1, 32),
    4: range(1, 31),
    5: range(1, 32),
    6: range(1, 31),
    7: range(1, 32),
    8: range(1, 32),
    9: range(1, 31),
    10: range(1, 32),
    11: range(1, 31),
    12: range(1, 32),
}

from datetime import datetime




def parse_data(date: str) -> bool:
    d, m, y = map(int, date.split('.'))
    return _y_is_valid(y) and _m_is_valid(m) and _d_is_valid(d, m, y)


def _d_is_valid(d: int, m: int, y: int) -> bool:
    if _is_leap_year(y) and m == 2:
        return d in range(1, 30)
    return d in __MONTHS[m]


def _m_is_valid(m: int) -> bool:
    return m in range(1, 13)


def _y_is_valid(y: int) -> bool:
    return y in range(1, 10_000)


def _is_leap_year(y: int) -> bool:
    return y % 4 == 0 and y % 100 != 0 or y % 400 == 0


if __name__ == '__main__':
    _d = datetime(2000, 2, 20)
    print(_d)
