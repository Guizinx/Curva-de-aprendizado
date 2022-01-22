import Validador_e_Gerador_CNPJ
import Desafio_valide_um_CNPJ

cnpj=input(str('Digite seu cnpj:'))
cnpj1=Desafio_valide_um_CNPJ.re.sub(r'[^0-9]','',cnpj)


novo_cnpj = Desafio_valide_um_CNPJ.validacao(cnpj)

if novo_cnpj == cnpj1:
    print('Válido')
else:
    print('Invalido')

print ( f'CNPJ válido gerado {Validador_e_Gerador_CNPJ.gera()}')
