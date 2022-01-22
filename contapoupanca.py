from aula113 import conta

class ContaPoupanca(conta):
    def sacar(self,valor):
        if self.saldo < valor:
            print('saldo insuficiente')
            return

        self.saldo -= valor
        self.detalhes()