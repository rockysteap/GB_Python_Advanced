f = open('text_data.txt')  # , encoding='utf-8')
print(f)  # <_io.TextIOWrapper name='text_data.txt' mode='r' encoding='cp1251'>
print(list(f))

# ['Lorem ipsum ....\n', 'РџСЂРёРІРµС‚ РјРёСЂ!\n']
f.close()

# UTF (Unicode Transformation Format)
# 🔥 Важно! Кодировка UTF-8 является современным стандартом для хранения и передачи текстовой информации.
# Если вы явно не планируете работать с другой кодировкой, всегда указывайте encoding='utf-8' при открытии
# текстовых файлов. Это обеспечит переносимость вашего кода между различными платформами.

print()
f = open('text_data.txt', encoding='utf-8')
print(f)  # <_io.TextIOWrapper name='text_data.txt' mode='r' encoding='utf-8'>
print(list(f))

# ['Lorem ipsum ....\n', 'Привет мир!\n']
f.close()
