# Функции setattr(), getattr() и delattr()

# В примере выше мы вызвали функцию setattr для присвоения у объекта self свойству item значения 0.
# В Python есть функции, которые позволяют делать то же, что и рассмотренные выше дандер методы.
# Разница лишь в том, что метод реагирует на событие в коде, а функцию вы вызываете в тот момент,
# когда вам это нужно.

# ● setattr(object, name, value) — аналог object.name = value
# ● getattr(object, name[, default]) — аналог object.name or default
# ● delattr(object, name) — аналог del object.name
