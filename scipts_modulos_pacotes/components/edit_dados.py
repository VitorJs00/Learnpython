def Editar(computador_1,opcoes):
    computador = computador_1
    total_escolhas = []
    print(f"------EDITAR DADOS------")
    try:
        for opcao,n in zip(opcoes,list(range(len(opcoes)))):
            print(f'{n+1}:{opcao}')
        escolha = input('DIGITE O NUMERO DA OPCAO:')
        escolha = opcoes[(int(escolha)-1)]
        try:
            especificacao= computador['configuracao'][escolha]
            if type(especificacao) != str and len(especificacao)>1:

                parametros = list(especificacao.keys())
                parametro_2 = input(f'Qual parametro?\n {parametros}')
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
                    computador['configuracao'].pop(escolha)
                    total_escolhas.pop(total_escolhas.index(escolha))
                    
                else:    
                    especificacao = novo_valor
                    print(f'{escolha}:{especificacao}')
                
            else:
                print('invalido!')
            
        except:
            if escolha in computador and escolha!= 'configuracoes':
                print(f'editando:{escolha}')
                novo_valor = input('insira o novo valor !, ou [↪] Para excluir' )
                if novo_valor =='':
                        ...
                else:    
                    computador.update({str(escolha):str(novo_valor)})
                    print(f'ALTERADO: {escolha}:{computador[escolha]}')

            else:
                print('Valor invalido')

    except:
        return f"ENTRADA INVALIDA"
    

    return computador

def get_opcoes(computador:dict)->list:
    opcoes = []
    for element  in computador['configuracao']:
        opcoes.append(element)
    total_escolhas =   opcoes.copy() 
    for key in computador.keys():
        total_escolhas.insert(0,key)
    total_escolhas.remove('configuracao')
    return total_escolhas



def get_info(computador,chave):
    
    try:
        parametro = computador[chave]
        mensagem = f"-----INFO-----\ndados:\n\t{chave} \t {parametro}"
        return mensagem
    
    except:
        mensagem = f"-----INFO-----\ndados:{chave}\n"
        parametro = computador['configuracao'][chave]
        if parametro == dict:
            for info in parametro:
                mensagem+= f'\t{info}:{parametro[info]}\n'
        else:
            mensagem = f"-----INFO-----\ndados:\n\t{chave} : {parametro}"
        return mensagem
