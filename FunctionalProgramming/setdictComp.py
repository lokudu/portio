#list, set dictionary
simple_dict ={
    'a': 1,
    'b': 2
}
my_dict = {k:v**2 for k, v in simple_dict.items() if v%2 ==0}

my_dict2 = {num:num*2 for num in [1,2,3]}

print(my_dict)
print(my_dict2)