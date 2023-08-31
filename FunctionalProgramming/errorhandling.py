# Error Handling
while True:
    try:
        age = int(input('what is your age? '))
        10/age
    except ValueError:
        print('please enter a number')
        continue
    except ZeroDivisionError:
        print('please enter a age higher than 0')
        break
    else:
        print(age)
        break
    finally:
        print('ok, i am finally done')