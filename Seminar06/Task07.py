# Создайте модуль и напишите в нём функцию,
# которая получает на вход дату в формате DD.MM.YYYY и возвращает истину,
# если дата может существовать или ложь, если такая дата невозможна.

# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# И весь период действует григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

from data_parser import parse_data as pd

print(pd('28.02.2000'))
print(pd('29.02.2024'))
print(pd('28.02.1900'))
print(pd('28.02.0001'))
print(pd('30.12.2010'))
