condicao =True
passou_if = None

if condicao:
    passou_if = True
    print('passou no if')
else:
    print('nao passou no if')
print(passou_if, passou_if is None)
print(passou_if, passou_if is not  None)


numero= input('digite um numero inteiro')
try:
    if int(numero)%2 == 0:
        print('par')
    else:
        print('impar')
except:
   print('valor nao é valido')


horario= input('digite a hora: XX:XX')
hora = horario[:2:]
try:
    hora_int  = int(hora)
    if 0 <=hora_int<=23:
        if  0<=int(hora_int)<=11:
            print('bom dia')
        elif 12<=hora_int<=17:
            print('boa tarde')
        else:
            print('boa noite')
    else:
        print('hora invalida')
except:
    print('insira um horario valido!')



user= input('nome')
if user:
    if len(user)<=4:
        print('seu nome é curto')
    elif len(user)<=6 and len(user)>=5: 
        print('medio')
    else:
        print('grande')
else:
    print('invalido')