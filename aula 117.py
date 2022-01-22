class A:
    def __new__(cls, *args, **kwargs):

        return super().__new__(cls)

    def __init__(self):
        print('Eu sou INIT')

a=A()
