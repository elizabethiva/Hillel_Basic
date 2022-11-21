data = input('Type list: ')
lst = list(data)
if len(lst) == 0 or 1:
    print(lst)
else:
    lst.insert(0, lst[-1])
    del(lst[-1])
    print(lst)
