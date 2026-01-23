def dividir(n1,n2):
    return n1/n2

try:
    #CODIGO QUE É TESTADO
    n_1=int(input('1* numero'))
    n_2=int(input('2* numero'))
    print(dividir(n_1,n_2))
except (ZeroDivisionError,TypeError) as e:
    print(f'erro:{e}')

except Exception:
    #CODIGO EXECUTADO SE DER ERRO
    print(f'deu pau ')
else:
    #EXECUTADO SE NAO HOUVER ERRO
    print('NAO HOUVE ERRO')
finally:
    #SEMPRE EXECUTADO
    print('fim do programa')
 