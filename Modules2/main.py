from utility import multiply, divide
from shopping.more_shopping.shopping_cart import buy
from random import choice, shuffle #build in modules
import sys

if __name__ == '__main__':
    print(buy('apple'))
    print(multiply(5*3, 6))
    print(divide(5/2, 1))
    print(max(1,2,3,4,2,3,10))

    print('please run this')

    print(choice([1,2,3,4,5,6]))

    my_list = [1,2,3,4,5]
    shuffle(my_list)
    print(my_list)

    print(sys.version)