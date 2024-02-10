# JSON (JavaScript Object Notation) — это популярный формат текстовых данных,
# который используется для обмена данными в современных веб- и мобильных приложениях.

# Кроме того, JSON используется для хранения неструктурированных
# данных в файлах журналов или базах данных NoSQL.

# Несмотря на JavaScript в названии формат JSON не привязывается к конкретному ЯП.
# Созданный на Python JSON может быть прочитан приложением Android на Java и iOS на Swift.
# Как результат JSON стал одним из самых популярных форматов передачи данных.

# Формат JSON (пример):
# {
#     "id": 2,
#     "name": "Ervin Howell",
#     "username": "Antonette",
#     "email": [
#         "Shanna@melissa.tv",
#         "antonette@howel.com"
#     ],
#     "address": {
#         "street": "Victor Plains",
#         "suite": "Suite 879",
#         "city": "Wisokyburgh",
#         "zipcode": "90566-7771",
#         "geo": {
#             "lat": "-43.9509",
#             "lng": "-34.4618"
#         }
#     },
#     "phone": "010-692-6593 x09125",
#         "website": "anastasia.net",
#         "company": {
#         "name": "Deckow-Crist",
#         "catchPhrase": "Proactive didactic contingency",
#         "bs": "synergize scalable supply-chains"
#     }
# }

# Как несложно заметить JSON похож на словарь Python.
# Но, при конвертации словаря в JSON и последующей конвертации в словарь типы данных могут оказаться иными.

#    Python    |     JSON     |   Python
#     dict          object         dict
#   list,tuple      array          list
#     str           string         str
#     int         number(int)      int
#     float       number(real)     float
#     True          true           True
#     False         false          False
#     None          null           None

# *list и tuple конвертируется в массив array, а при обратной конвертации получаем только list.
# Если мы храним несколько JSON объектов, в Python обычно используют list.
# Для JSON в этом случае используется array — в квадратных скобках записываются JSON объекты разделённые запятыми.



