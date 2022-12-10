#Напишите фукцию common_elements, которая сгенерирует два списка с разным количеством элементов (кол-во задается параметром функции).
# Один список с числами кратными 3, другой с числами кратными 5.
# С помощью множеств создайте набор с числами, которые есть в обоих множествах (пересечение).
# Функция должна вернуть это множество в качестве результата своей работы.
import random
def common_elements(a, b, c, d):
    first_list = [random.randint(1, 100) for i in range(random.randint(a, b))]
    x = set()
    for i in first_list:
        if i % 3 == 0:
            x.add(i)
    second_list = [random.randint(1, 100) for i in range(random.randint(c, d))]
    y = set()
    for a in second_list:
        if a % 5 == 0:
            y.add(a)
    z = x.intersection(y)
    return z
d = common_elements(1, 21, 5, 25)
print(d)
