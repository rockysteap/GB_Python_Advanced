rows = int(input('Введите количество рядов ёлки: '))

for i in range(rows):
    print(f'{" " * (rows - i)}{"*" * (1 + 2 * i)}')
