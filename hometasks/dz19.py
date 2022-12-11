import random

def common_elements(size_1, size_2):
    first_list = []
    while len(first_list) != size_1:
        x = random.randint(0, 100)
        if x % 3 == 0:
            first_list.append(x)
    first_set = set(first_list)
    second_list = []
    while len(second_list) != size_2:
        x = random.randint(0, 100)
        if x % 5 == 0:
            second_list.append(x)
    second_set = set(second_list)
    intersection = first_set.intersection(second_list)
    return intersection
intersection = common_elements(100, 100)
print(intersection)
