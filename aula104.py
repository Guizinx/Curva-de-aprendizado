"""
public, protected, private
"""

class BaseDeDados:
    def __init__(self):
        self.dados = {}

    def inserir_cliente(self,id,nome):
        if 'clientes' not in self.dados:
            self.dados['clientes'] = {id: nome}
        else:
            self.dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id , nome in self.dados['clientes'].items():
            print(id,nome)

    def apaga_cliente(self, id):
        del self.dados['clientes'][id]

bd = BaseDeDados()
bd.inserir_cliente(1,'Otavio')
bd.inserir_cliente(2,'Ronaldo')
bd.inserir_cliente(3,'Rose')
bd.apaga_cliente(2)
bd.lista_clientes()

