"""
data = {10, 9, 8, 1, 6, 3}
a, b, c, *d, e = data
print(a, b, c, d, e)  # 1 3 6 [8, 9] 10
"""

"""
data = {"один": 1, "два": 2, "три": 3}
x = iter(data.items())
print(x)  # iter_object
y = next(x)
print(y)  # 'один': 1
z = next(iter(y))  # создается новый объект итератор от кортежа y
print(z)  # 'один'
"""

"""
data = {2, 4, 4, 6, 8, 10, 12}
res1 = {None: item for item in data if item > 4}
res2 = (item for item in data if item > 4)
res3 = [[item] for item in data if item > 4]
print(res1, res2, res3)
# {None: 12}
# <generator object <genexpr> at 0x0000019038C736B0>
# [[6], [8], [10], [12]]
"""


def gen(a: int, b: int) -> str:
    if a > b:
        a, b = b, a
    for i in range(a, b + 1):
        yield str(i)


for item in gen(10, 1):
    print(f'{item = }')
