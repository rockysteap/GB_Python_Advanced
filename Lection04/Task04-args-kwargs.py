def mean(args):
    return sum(args) / len(args)


print(mean([1, 2, 3]))
# print(mean(1, 2, 3))  # TypeError: mean() takes 1 positional argument but 3 were given


def mean(*args):
    return sum(args) / len(args)


print(mean(*[1, 2, 3]))
print(mean(1, 2, 3))


def school_print(**kwargs):
    for key, value in kwargs.items():
        print(f'По предмету "{key}" получена оценка {value}')


school_print(химия=5, физика=4, математика=5, физра=5)
