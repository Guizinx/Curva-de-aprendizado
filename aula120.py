class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)
        print(namespace)

        return type.__new__(mcs,name,bases,namespace)


class A(metaclass=Meta):
    def fala(self):
        self.b_fala()

class B(A):
    def b_fala(self):
        print('Oi')


b = B()
b.fala()

