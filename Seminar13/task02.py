# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и значение по умолчанию.
# При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.

def getvalue(dictionary, key, default_value=None):
    try:
        return dictionary[key]
    except KeyError:
        return default_value


my_dict = {'one': 1, 'two': 2, 'three': 3}

print(getvalue(my_dict, 'two'))
print(getvalue(my_dict, "twelve", default_value=12))
