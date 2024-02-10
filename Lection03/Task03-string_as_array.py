text = 'однажды в СТУДЁНУЮ зИмнЮЮ ПоРУ'
print(text.upper())  # ОДНАЖДЫ В СТУДЁНУЮ ЗИМНЮЮ ПОРУ
print(text.lower())  # однажды в студёную зимнюю пору
print(text.title())  # Однажды В Студёную Зимнюю Пору
print(text.capitalize())  # Однажды в студёную зимнюю пору

print()
text = 'Однажды в студёную зимнюю пору'
print(text.startswith('Однажды'))  # True
print(text.endswith('зимнюю', 0, -5))  # True

print()
text = 'Привет, мир!'
print(text.find(' '))  # 7
print(text.title())  # Привет, Мир!
print(text.split())  # ['Привет,', 'мир!']
print(f'{text=:>25}')  # text=             Привет, мир!
