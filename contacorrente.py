from aula113 import conta

class ContaCorrente(conta):
    def __init__(self,agencia,conta,saldo,limite =1000):
        super().__init__(agencia,conta,saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite


    def sacar(self,valor):
        if (self.saldo)+self.limite < valor:
            print('saldo insuficiente')
            return

        self.saldo -= valor
        self.detalhes()