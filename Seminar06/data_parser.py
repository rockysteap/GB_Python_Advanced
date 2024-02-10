from datetime import datetime

__all__ = ['parse_data']

_M29, _M31, _M32 = range(1, 29), range(1, 31), range(1, 32)
_MONTHS = {1: _M32, 2: _M29, 3: _M32, 4: _M31, 5: _M32, 6: _M31,
           7: _M32, 8: _M32, 9: _M31, 10: _M32, 11: _M31, 12: _M32, }


def parse_data(date: str) -> bool:
    d, m, y = map(int, date.split('.'))
    return _y_is_valid(y) and _m_is_valid(m) and _d_is_valid(d, m, y)


def _d_is_valid(d: int, m: int, y: int) -> bool:
    if _is_leap_year(y) and m == 2:
        return d in range(1, 30)
    return d in _MONTHS[m]


def _m_is_valid(m: int) -> bool:
    return m in range(1, 13)


def _y_is_valid(y: int) -> bool:
    return y in range(1, 10_000)


def _is_leap_year(y: int) -> bool:
    return y % 400 == 0 or y % 4 == 0 and y % 100 != 0


if __name__ == '__main__':
    __d = datetime(2000, 2, 20)
    print(__d)
