lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
x = lst.count(0)
print(x)
del(lst[0])
print(lst)
lst2 = [0] * (x-1)
lst.extend(lst2)
print(lst)
