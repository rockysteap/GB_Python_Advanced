# for i in range(2, 10, 4):
for i in [2, 6]:
    for j in range(2, 11):
        for k in range(i, i + 4):
            print(f'{k:>2} x {j:>2} = {k * j:>2}', end='\t')
        print()
    print()
