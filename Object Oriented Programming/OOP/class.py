# my First class


class PlayerCharacter:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')
        return 'done'


player1 = PlayerCharacter('lokudu', 32)
player2 = PlayerCharacter('Alex', 18)

print(player1.age)
print(player2.age)
print(player1.run())