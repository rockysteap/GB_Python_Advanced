from random import randint, uniform

MIN_NUM = -1000
MAX_NUM = 1000


def write_numbers(name, rows):
    with open(name, 'w') as f:
        for i in range(rows):
            f.write(f'{randint(MIN_NUM, MAX_NUM):>5} | {uniform(MIN_NUM, MAX_NUM)}\n')


if __name__ == '__main__':
    write_numbers('numbers.txt', 7)
