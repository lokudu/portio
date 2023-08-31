class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f'my name is {self.name},and am {self.age} years old')


player1 = PlayerCharacter('Lokudu', 20)
player1.speak()


