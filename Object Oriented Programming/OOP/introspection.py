class User():
    def __init__(self, email):
        self.email = email

    def signed_in(self):
        print("User is logged in.")

    def attack(self):
        print("Do nothing.")


class Wizard(User):
    def __init__(self, name, power, email):
        self.name = name
        self.power = power
        super().__init__(email)  # same as using the below command, it does not take 'self' parameter
        # User.__init__(self, email)

    def attack(self):
        print(f"{self.name} is attacking with {self.power} power.")


wizard1 = Wizard("John", 50, 'john@gmail.com')
print(dir(wizard1.email))
