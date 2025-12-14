computador = {
    'configuracao':{
        'placa_de_video':{
            'nome':'RTX 3090',
            'fabricante':'NVIDIA',
            'ano':'2023',

        },
        'processador':{
            'nome':'Ryzen 5600X',
            'fabricante':'AMD',
            'ano':'2017',

        },
        'quantidade_fan':3,
        'ram':{
            'total_capacidade':'16gb',
            'mhz':'2666mhz'
        },
        'cooler':'Whater Plus',
        'fonte':{
            'fabricante':'Turbilhao PRO',
            'ano':'2019',
            'potencia':'700w'
        },
        'armazenamento':[
            {
                'fabricante':'YYYYYY',
                'ano':'YYYY', 
                'capacidade':'480gb',
                'tipo':'ssd'
            },
            {   
                'fabricante':'KKKKKK',
                'ano':'KKKK', 
                'capacidade':'1t',
                'tipo':'nvme'
            }
        ]
    },
    'preço':3999.00,
    'consumo':'280w',
    'data_de_compra':'23-05-2021'
}
opcoes = []

for element  in computador['configuracao']:
    opcoes.append(element)
total_escolhas =   opcoes.copy() 
for key in computador.keys():
    total_escolhas.insert(0,key)


rodando=True

while  rodando:
    try:
        escola = int(input('[1]Pesquisar|[2]Editar|[3]Sair'))

        if escola ==1:
            entrada = input('QUAL PARAMETRO QUER SABER?').lower()
            if entrada in opcoes:
                print(computador['configuracao'][entrada])
            elif entrada in computador:
                print(computador[entrada])
            else:
                print('Valor invalido')
                
        elif escola ==2:
            print(f'OPCOES:[{total_escolhas}]')

            parametro = input('Qual Area editar?')
            if parametro in opcoes:
                especificacao= computador['configuracao'][parametro]
                if type(especificacao) != str and len(especificacao)>1:
                    
                    parametro_2 = input(f'Qual parametro?[{especificacao}]')
                    if parametro_2 in especificacao:
                        print(f'editando {parametro_2}')
                        novo_valor = input('insira o novo valor !, ou [↪] Para excluir' )
                        if novo_valor =='':
                            del especificacao[parametro_2]
                        else:
                            especificacao[parametro_2] = novo_valor
                            print(f'ALTERADO {especificacao}')
                    else:
                        print(f'Nao exite {parametro_2} em {especificacao}')

                elif type(especificacao) == str :
                    print(f'editando {especificacao}')
                    novo_valor = input('insira o novo valor !, ou [↪] Para excluir' )
                    if novo_valor =='':
                        computador['configuracao'].pop(parametro)
                        total_escolhas.pop(total_escolhas.index(parametro))
                        
                    else:    
                        especificacao = novo_valor
                        print(f'{parametro}:{especificacao}')
                    
                else:
                    print('invalido!')
                    continue


            elif parametro in computador and parametro!= 'configuracoes':
                print(f'editando {computador[parametro]}')
                novo_valor = input('insira o novo valor !, ou [↪] Para excluir' )
                if novo_valor =='':
                        ...
                else:    
                    computador.update({str(parametro):str(novo_valor)})
                    print(f'ALTERADO {computador[parametro]}')

            else:
                print('Valor invalido')
        elif escola == 3:
                rodando=False
                break
    except:
        print('ERROR')
        rodando=False
