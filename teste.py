x =  int(input('indique um número inteiro:'))
y=0
z=0
primos = []
conferidor = 0
resto = []

if x == 1:
    print ("Não há números primos.")
elif y == 2:
    primos.append(2)
else:
    primos.append(2)
    for y in range (3,x+1,1):
        for z in range (2,y,1):
            if y % z == 0:
                conferidor = 1
        if conferidor == 1:
            conferidor = 0
        elif conferidor == 0:
            primos.append(y)
for w in primos:
    resto.append(x%w)

print(primos)
print(resto)

