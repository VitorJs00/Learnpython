nome= input('nome:')
idade= input('idade:')
if not (nome and idade):
    print('nada foi digitado')
    
else:
    print(f'seu nome é {nome[::-1]} e de {idade} anos')
    if not " " in nome:
        print('seu nome nao tem espaços')
    else:
        print('seu nome  tem espaços')
    print(f'seu nome tem:{len(nome)} letras')
    print(f'a primeira letra de seu nome é {nome[0]}')
    print(f'a ultima letra de seu nome é {nome[-1]}')