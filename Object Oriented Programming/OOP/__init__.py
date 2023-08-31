# my First class


class PlayerCharacter:
    # Class object Attribute
    membership = True

    def __init__(self, name = 'something', age = 0):
        if age > 18:
            self.name = name  # Attribute
            self.age = age

    def shout(self):
        print(f'my name is {self.name} and am {self.age} years old')
        return ''


player1 = PlayerCharacter('lokudu', 19)
player2 = PlayerCharacter('Alex', 18.5)
player2.attack = 70

print(player1.shout())
print(player2.shout())
