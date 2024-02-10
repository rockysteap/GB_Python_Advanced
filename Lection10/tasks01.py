class User:
    count = []

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


u1 = User('One', '123-45-67')
u2 = User('NoOne', '76-54-321')

u1.count.append(42)  # u1.count = [42]
u1.count.append(73)  # u1.count = [42, 73]

u2.counter = 256  # u2.counter = 256
u2.count.append(u2.counter)  # u2.count = [42, 73, 256] ->   # u1.count = [42, 73, 256]
u2.count.append(u1.count[-1])  # u2.count = [42, 73, 256, 256]  ->   # u1.count = [42, 73, 256, 256]

print(f'{u1.name = }, {u1.phone = }, {u1.count = }')
print(f'{u2.name = }, {u2.phone = }, {u2.count = }')
