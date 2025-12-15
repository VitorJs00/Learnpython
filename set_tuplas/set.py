A = set({1,2,3})
B = {2,3,4}
computador_2 ={
        3999,
        '280w',
}

computador_1 ={
        True,
        2.3,
}

print(A.intersection(B),A.union(B),A.difference(B),B.difference(A),computador_2.union(computador_1)) #A_inter_B

computador_1.add(2222)
computador_1.add(True)
print(computador_1)

computador_2.update({'280w','NOVO',2.3})
print(computador_2)

computador_1.discard('True') #se existir remove se nao -> NADA
print(computador_1)

computador_1.remove(2222)#remove somente se existir se nao ->error
print(computador_1)

computador_1.pop() #remove o ultimo elemento
print(computador_1)

computador_1.intersection_update(computador_2) #computador 1 = interceção
print(computador_1)


computador_2.clear()
print(computador_2)

mulher= {'ana','bia','clara'}
homem = {'arthur','bruno','carlos'}
olho_claro = {'ana','bruno','clara'}

print(f'mulher de olho claro = {olho_claro&mulher}')
print(f'nao olho claro={(homem|mulher).symmetric_difference(olho_claro)}')