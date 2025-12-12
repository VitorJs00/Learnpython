rodando= True
while rodando:

    try:
        idade= int(input('sua idade'))
        sexo = input('[M]masc [F]femi').lower()
    
        if sexo == 'm' or sexo =='f':
            rodando=False
            if sexo =='m' and idade >60:
                    print('CONCEDIDA!')
            
            elif sexo =='f' and idade>65:
                    print('CONCEDIDA!')
                    
            else:
                    print('nao ta no tempo. NEGADA!')
                   
        else:
            print('ENTRADA INVALIDA')
    except:
        print(f'a entrada é invalida, tente novamente')
