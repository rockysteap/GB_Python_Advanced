# Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор,
#   пока он не введёт целое или вещественное число.
# Обрабатывайте не числовые данные как исключения.

def get_number():
    while True:
        try:
            return float(input("Введите число: "))
        except ValueError as e:
            print(f"Ваш ввод привёл к ошибке ValueError: {e}")


print(get_number())
