#my_file = open('test.txt')

#print(my_file.read())

#my_file.close()
try:
    with open('dad.txt', mode='r') as my_file:
        text = my_file.write(':(')
        print(text)
except FileNotFoundError as err:
    print('File does not exist')
    raise err
