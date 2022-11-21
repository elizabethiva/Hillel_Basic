lst = [1, 2, 3, 4, 5, 6]
middle = len(lst) // 2
first_half = lst[:middle]
second_half = lst[middle:]
print(first_half, second_half)
lst2 = [1, 2, 3]
lst2_edit = lst.copy()
del(lst2_edit[0])
middle2 = len(lst2_edit) // 2
first_half2 = lst2_edit[lst2[0], :middle2]
second_half2 = lst2_edit[middle2:]
print(first_half2, second_half2)
