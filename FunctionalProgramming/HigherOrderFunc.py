# Higher Order Function HOC

def greet(func):
    func()


def greet2():
    def func():
        return 5

    return func
