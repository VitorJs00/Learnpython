lista_1 = ['str',True,5,4.5,['lista']]
lista_2 = []
for i in range(4,-1,-1):
    lista_2.append(i)


tab = []#3x3 = 9 elementos
for i in range(9):
    tab.append('NOT MATRIZ')

#print(f"{tab[0:3]}\n{tab[3:6]}\n{tab[6:9]}")



tab_2 = []
tamanho = 10
contador=1
for num in range(tamanho):
    tab_2.append([])


for linhas in range(tamanho):
    for colunas in range(tamanho):
        #tab_2[linhas].append(str(contador).zfill(2))
        tab_2[linhas].append('!')
        contador+=1
# linha e coluna       


#PINTANDO DIAGONAIS
for index_linha in range(tamanho):
    tab_2[index_linha][index_linha] = '?'
    tab_2[index_linha][-index_linha-1]='?'




#exibir tabela
for indice in range(tamanho):
    print(tab_2[indice])

 