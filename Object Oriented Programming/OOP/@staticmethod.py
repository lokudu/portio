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

    @staticmethod
    def adding_things(num1, num2):
        return num1 + num2


player3 = PlayerCharacter.adding_things(10, 30)

print(player3)
