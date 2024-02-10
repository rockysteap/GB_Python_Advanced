lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lst.insert(-1, 11)
print(lst)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 11, 9]


my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
print(my_list[2:6:2])  # [6, 8]
print(my_list.pop())  # 18
print(my_list.extend([314, 42]))  # None
print(my_list.sort(reverse=False))  # None
print(my_list)  # [2, 2, 4, 6, 8, 10, 12, 14, 16, 42, 314]

