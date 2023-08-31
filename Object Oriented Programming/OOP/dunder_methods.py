class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'lokudu',
            'has_pet': False
        }

    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    def __del__(self):
        print('deleted')

    def __call__(self):
        return 'years??'

    def __getitem__(self, item):
        return self.my_dict[item]

action_figure = Toy('Red', 0)

print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure['name'])
