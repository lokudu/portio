my_list = [1, 2, 3]


def multiply_by2(item):
    return item * 2


def check_odd(item):
    return item % 2 != 0


print(list(filter(check_odd, my_list)))
