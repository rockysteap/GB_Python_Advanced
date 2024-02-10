# Задание №8
# ✔ Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами.
# Код должен расширяться на любое большее количество друзей.

friends = {
    'Афанасий': ('аккордеон', 'бинокль', 'велосипед', 'настроение'),
    'Борис': ('аккордеон', 'бинокль', 'велосипед', 'настроение'),
    'Владимир': ('аккордеон', 'бинокль', 'велосипед', 'розетка', 'бритва'),
    'Григорий': ('аккордеон', 'бинокль', 'велосипед', 'настроение'),
    'Дмитрий': ('аккордеон', 'бинокль', 'велосипед', 'настроение'),
    'Егор': ('аккордеон', 'бинокль', 'велосипед', 'настроение'),
    'Емельян': ('аккордеон', 'бинокль', 'велосипед', 'настроение', 'удочка'),
}

all_items = []
for things in friends.values():
    all_items.extend(things)

unique_set_of_all_items = set(all_items)

non_matched_list = []
for v in friends.values():
    non_matched = unique_set_of_all_items.difference(set(v))
    non_matched_list.extend(non_matched)
    # print(non_matched)

items_got_everyone_except_one = []
items_got_only_one = []

for non_matched_item in set(non_matched_list):
    if non_matched_list.count(non_matched_item) > 1:
        items_got_only_one.append(non_matched_item)
    else:
        items_got_everyone_except_one.append(non_matched_item)

# print(items_got_only_one)
# print(items_got_everyone_except_one)

for i in items_got_only_one:
    for k, v in friends.items():
        if i in v:
            print(f'Уникальная вещь - {i}, владелец {k}.')

for i in items_got_everyone_except_one:
    for k, v in friends.items():
        if i not in v:
            print(f'Есть у всех - {i}, но {k} не имеет.')




"""
# Решение на семинаре:

# Три друга взяли вещи в поход. Сформируйте словарь,
# где ключ - имя друга, а значение - кортеж вещей. Ответьте на вопросы:

# какие вещи взяли все три друга

# какие вещи уникальны, есть только у одного друга

# какие вещи есть у всех друзей кроме одного и имя того,
# у кого данная вещь отсутствует

# Для решения используйте операции с множествами.
# Код должен расширяться на любое большее количество друзей.

hike = {
    'Aaz': ("спички", "спальник", "дрова", "топор"),
    'Skeeve': ("спальник", "спички", "вода", "еда"),
    'Tananda': ("вода", "спички", "косметичка"),
}

temp_bag = None
for things in hike.values():
    if not temp_bag:
        temp_bag = set(things)
        continue
    temp_bag = temp_bag.intersection(set(things))
print(temp_bag)


result_uniq = {}
for name, things in hike.items():
    temp = set(things)
    temp_o = set()
    for other in hike.values():
        if things == other:
            continue
        temp_o = temp_o.union(set(other))
    temp = temp.difference(temp_o)
    if temp:
        result_uniq.update({name: temp})
print(result_uniq)


res_missing = {}
for name, things in hike.items():
    temp = set(things)
    for other in hike.values():
        if things == other:
            continue
        temp_o = temp_o.intersection(set(other))
    temp = temp_o.difference(temp)
    if temp:
        res_missing.update({name: temp})

print(res_missing)
"""