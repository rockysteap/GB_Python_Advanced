# Задание №2
# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.

def string_to_unicode(string: str) -> list[int]:
    return sorted(set(list(map(lambda c: ord(c), string))), reverse=True)


s = 'Напишите функцию, которая принимает строку текста.'
print(string_to_unicode(s))
