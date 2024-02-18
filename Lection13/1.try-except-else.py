# 🔥 Важно!
# Блок кода внутри try в идеале должен состоять из одной строки кода — потенциального источника ошибки.
# Оборачивание всей программы в блок try считается плохим стилем программирования.

# Внимание! Язык Python поддерживает такие математические числа как
# бесконечность и минус бесконечность.
# Записываются они как особая форма вещественного числа:
# ● float(‘inf’) - бесконечность
# ● float(‘-inf’) - минус бесконечность

"""
def get(text: str = None) -> int:
    while True:
        try:
            num = int(input(text))
            break
        except ValueError as e:
            print(f'Ваш ввод привёл к ошибке ValueError: {e}\n' f'Попробуйте снова')
    return num


if __name__ == '__main__':
    number = get('Введите целый делитель: ')
    print(f'100 / {number} = {100 / number}')
"""

# Команда else
# Если надо выполнить код только в случае успешного завершения блока try, можно
# воспользоваться командой else в связке try-except-else
MAX_COUNT = 5
result = None
for count in range(1, MAX_COUNT + 1):
    try:
        num = int(input('Введите целое число: '))
        print('Успешно получили целое число')
    except ValueError as e:
        print(f'Попытка {count} из {MAX_COUNT} завершилась ошибкой {e}')
    else:
        result = 100 / num
        break
print(f'{result = }')

# Блок else не сработает, если внутри try произошло любое из событий:
# возбуждено исключение
# выполнена команда return
# выполнена команда break
# выполнена команда continue