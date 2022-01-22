
def lista_de_clientes(clientes_iteravel, lista=[]):
    lista.extend(clientes_iteravel)
    return lista

clientes1=lista_de_clientes(['João', 'Maria', 'Chales'])
clientes2= lista_de_clientes(['Marcos', 'Jonas', 'Zico'])

print(clientes1)
print(clientes2)