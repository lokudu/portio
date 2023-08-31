# my First class


class PlayerCharacter:
    # Class object Attribute
    membership = True

    def __init__(self, name, age):
        if PlayerCharacter.membership:
            self.name = name  # Attribute
            self.age = age

    def shout(self):
        print(f'my name is {self.name} and am {self.age} years old')
        return ''


player1 = PlayerCharacter('lokudu', 32)
player2 = PlayerCharacter('Alex', 18)
player2.attack = 70

print(player1.shout())
print(player2.shout())
