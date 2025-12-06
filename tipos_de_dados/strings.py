nome = "Travis            "
sobrenome = "Scott"
nome_completo = nome +' '+ sobrenome
valor = 369.2468
#print(nome_completo)
nome_completo = nome.strip() +' '+ sobrenome
#print(nome_completo)
#print(nome_completo.lower())
#print(nome_completo.upper())
#print (nome_completo + '\num dos melhores artistas na minha opinião' )
#print ('\t'+nome_completo + ' um dos melhores artistas na minha opinião  \' ' )

#metodo format

print('O melhor Artista é {nome} {sobrenome}'.format(nome=nome.strip(), sobrenome=sobrenome))
print(f'O melhor Artista é {nome_completo}')
print('Explorando o format com float {num:.2f}'.format(num = valor))