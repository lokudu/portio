def check():
    age = input('What is your age? ')#string
    if int(age) < 18:#convert to interger
        print('you are under age')
    elif int(age) > 18:
        print('you can watch')
    elif int(age) == 18:
        print('congratulations')
check()