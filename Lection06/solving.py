import random
from sys import argv

print(random.uniform(int(argv[1]), int(argv[2])))
print(random.randrange(int(argv[1]), int(argv[2]), int(argv[1])))
print(random.sample(range(int(argv[1]), int(argv[2]), int(argv[1])), 10))

# Скрипт запущен командой: python3 main.py 10 1010
