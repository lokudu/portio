# Error Handling
while True:
    try:
        age = int(input('what is your age? '))
        10/age
        raise Exception('hey cut it out')

    except ZeroDivisionError:
        print('please enter a age higher than 0')
        break
    else:
        print(age)

    finally:
        print('ok, i am finally done')