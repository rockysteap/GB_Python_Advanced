
# def func(a=0.0, /, b=0.0, *, c=0.0):
#     """func(a=0.0: int | float, /, b=0.0: int | float, *, c=0.0:int | float) -> : int | float"""
#     if a > c:
#         return a
#     if a < c:
#         return c
#     return
#
#
# print(func(c=1, b=2, a=3))
# TypeError: func() got some positional-only arguments passed as keyword arguments: 'a'


data = [25, -42, 146, 73, -100, 12]

print(list(map(str, data)))
# ['25', '-42', '146', '73', '-100', '12']

print(max(data, key=lambda x: -x))
# -100

print(*filter(lambda x: not x[0].startswith('__'), globals().items()))
# ('data', [25, -42, 146, 73, -100, 12])
