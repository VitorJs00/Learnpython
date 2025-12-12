rodando = True

while rodando:
    try:
        while rodando:
            n1=int(input('numero 1'))
            operaçao= input('[+],[-],[*],[/]')
            n2=int(input('segundo numero'))

            if operaçao =='+':
                print(n1+n2)
            elif operaçao =='-':
                print(n1-n2)
            elif operaçao =='*':
                print(n1*n2)
            elif operaçao =='/':
                print(n1/n2)
            else:
                print('operaçao invalida')
            
            sair=False
            while sair ==False : 
                sair = input('[S] para sair [N] novamente')
                
                if sair=='s':
                    rodando=False
                    sair=True
                elif sair =='n':
                    
                    sair=True
                else:
                    sair=False
                 
    except:
            print('insira um numero valido')

