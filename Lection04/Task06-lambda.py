def add_two_def(a, b):
    return a + b


add_two_lambda = lambda a, b: a + b  # Так делать нельзя, lambda - анонимная функция
print(add_two_def(42, 3.14))
print(add_two_lambda(42, 3.14))

#  🔥 Важно! С точки зрения разработки присваивание анонимной функции
# имени является неверным. Лямбды не должны использоваться для подобных
# программных решений. Аналогичное предупреждение есть и в PEP-8.


my_dict = {'two': 2, 'one': 1, 'four': 4, 'three': 3, 'ten': 10}
s_key = sorted(my_dict.items())
s_value = sorted(my_dict.items(), key=lambda x: x[1])
print(f'{s_key = }\n{s_value = }')
