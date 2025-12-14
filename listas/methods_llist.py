lista = ['a','b','c','d','e']

lista.append('2')
lista.insert(0,'A')
lista.extend(['outra lista'])

print(lista)
lista.remove('b') #remove elementos e repetidos
print(lista)
lista.pop() #Remove o ultimo elemento
print(lista)
print(lista.index('c',0,3))
lista.reverse()
print(lista)
copia = lista.copy()
del copia[0] #remove elemento do index [0]
print(copia)