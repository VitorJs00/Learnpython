"""
Ordenadas
Permite duplicaçao
indexadas
Elementos nao-intercambiaveis(nao permite update/delete)
"""
lista = [2,'txt',4]
tupla_1 = (True,0,'ola',4.3)
tupla_2 = tuple(lista)
print(tupla_1[2])
print(tupla_2[tupla_2.index('txt')])
print(tupla_1[1:3])
print(tupla_1.count(True))

