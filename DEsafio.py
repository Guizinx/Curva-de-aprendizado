i =0
verificador = 0
while i == False or verificador != 9:
    CPF = str(input('Digite os 9 primeiros números do CPF (apenas os números):'))
    verificador = len(CPF)
    try:
        CPF1 = int(CPF)
        i = True
    except:
        i = False
        print('Tente novamente')
a=10
CPF = list(str(CPF))
valor_somatorio = 0
for multiplicador in CPF:
    multiplicador = int(multiplicador)
    valor_unitario = multiplicador * a
    valor_somatorio = valor_somatorio + valor_unitario
    a -= 1

digito1 = 11 - (valor_somatorio % 11)
if digito1>9:
    digito1 = 0
print(f"o primeiro digito será {digito1}")
a=11
valor_somatorio=0
for multiplicador2 in CPF:
    multiplicador2 = int(multiplicador2)
    valor_unitario2 = multiplicador2 * a
    valor_somatorio = valor_somatorio + valor_unitario2
    a -= 1
    multiplicador2= str(multiplicador2)

valor_somatorio = valor_somatorio + (digito1*a)
digito2 = 11 - (valor_somatorio % 11)
if digito2>9:
    digito2 = 0
print(f'o segundo digito será {digito2}')
CPF.append(str('-'))
CPF.append(str(digito1))
CPF.append(str(digito2))

CPF1="".join(CPF)
print (f"Seu cpf completo será {CPF1}")
