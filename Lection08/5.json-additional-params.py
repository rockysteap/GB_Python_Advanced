import json

my_dict = {
    "id": 123,
    "name": "Clementine Bauche",
    "username": "Cleba",
    "email": "cleba@corp.mail.ru",
    "address": {
        "street": "Central",
        "city": "Metropolis",
        "zipcode": "123456"
    },
    "phone": "+7-999-123-45-67"
}
res = json.dumps(my_dict, indent=2, separators=(',', ':'), sort_keys=True)

# ➢ Параметр indent отвечает за форматирование с отступами.
#       Теперь JSON выводится не в одну строку, а в несколько.
#       Читать стало удобнее, но размер увеличился.
# ➢ Параметр separators принимает на вход кортеж из двух строковых элементов.
#       Первый — символ разделитель элементов. По умолчанию это запятая и пробел.
#       Второй — разделитель ключа и значения. По умолчанию это двоеточие и пробел.
#       Передав запятую и двоеточие без пробела JSON стал компактнее.
# ➢ Параметр sort_keys отвечает за сортировку ключей по алфавиту.

print(res)
# {
#   "address":{
#     "city":"Metropolis",
#     "street":"Central",
#     "zipcode":"123456"
#   },
#   "email":"cleba@corp.mail.ru",
#   "id":123,
#   "name":"Clementine Bauche",
#   "phone":"+7-999-123-45-67",
#   "username":"Cleba"
# }
