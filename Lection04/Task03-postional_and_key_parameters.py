# Косая черта не является переменной. Это символ разделитель.
# После неё могут идти как позиционные, так и ключевые параметры.
# Далее символ разделитель звёздочка указывает только на ключевые параметры.

def func(positional_only_parameters, /, positional_or_keyword_parameters, *, keyword_only_parameters):
    pass


# ● Пример обычной функции:
def standard_arg(arg):
    print(arg)  # Принтим для примера, а не для привычки


standard_arg(42)
standard_arg(arg=42)


# ● Пример только позиционной функции:
def pos_only_arg(arg, /):
    print(arg)  # Принтим для примера, а не для привычки


pos_only_arg(42)


# pos_only_arg(arg=42)  # TypeError:
# pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'


# ● Пример функции со всеми вариантами параметров:
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)  # Принтим для примера, а не для привычки


# combined_example(1, 2, 3) # TypeError:
# combined_example() takes 2 positional arguments but 3 were given
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)


# combined_example(pos_only=1, standard=2, kwd_only=3) # TypeError:
# combined_example() got some positional-only arguments passed as keyword arguments: 'pos_only'


# 🔥 Важно! Если функция принимает несколько ключевых параметров, порядок передачи аргументов может отличаться
def triangulation(*, x, y, z):
    pass


triangulation(y=5, z=2, x=11)
