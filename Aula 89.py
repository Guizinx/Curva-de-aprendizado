file = open('abc.txt','w+')
file.write('Linha1\n')
file.write('Linha2\n')
file.write('Linha3\n')

file.seek(0,0)
print('Lendo linhas:')
print(file.read())

file.seek(0,0)
print(file.readline(), end =' ')
print(file.readline())

file.close()
