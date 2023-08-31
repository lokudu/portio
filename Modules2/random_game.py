from random import randint

# generate a number 1-10
answer = randint(1, 10)
# Ask input from users

# check if a right guess, otherwise ask again

while True:
    print(answer)

    guess = int(input('Guess a number from 1-10: '))
    try:
        if 0 < guess < 11:
            if guess == answer:
                print('You are a genius')
                break
        else:
            print('you fail terribly')
    except ValueError:
        print('Please enter a number')
        continue
