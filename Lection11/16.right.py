# Right методы срабатывают в том случае,
# если у левого аргумента в выражении метод не был найден.

# Например, при записи x + y вначале производится поиска дандер метода x.__add__.
# Если он не найден, вызываем y.__radd__.
