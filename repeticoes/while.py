"""
nome= input('digite algom')
while not nome:
    nome= input('digite algom')
print(f'o que digitou {nome}')


i=0
while i<=40:
     
    if i%2 ==0:  
        continue
    else:
        print(i)

linhas = 5
colunas =5
linha =0
while linha <=linhas:
    coluna=0
    while coluna<=colunas:
        print((f'{linha=}'),(f'{coluna}coluna'))
        coluna+=1
    linha+=1
    


nome = "OLOKO"
nova_string = ''
i=0
while i < len(nome):
    nova_string+= f'*{nome[i]}'
    i+=1
print(nova_string)

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

"""
text ='vitovr'
i=0
qtd=0
while i < len(text):
    letra= text[i]
    if letra ==' ':
        i+=1
        continue
    contando_letra=text.count(letra)
    if contando_letra >= qtd:
        qtd=contando_letra
        letra_max =[ letra, qtd]
    i+=1
print(letra_max)