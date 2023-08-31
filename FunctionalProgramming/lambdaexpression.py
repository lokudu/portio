from functools import reduce

my_list = [1, 2, 3]


def multiply_by2(item):
    return item * 2


def check_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    return acc + item


print(list(map(lambda item: item*2, my_list))) # filter, reduce and zip
