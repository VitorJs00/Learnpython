import datetime 
data =datetime.date.today()


def dados_computador(preco,consumo,*nota,data_compra=data,**configuracao):
    print(f'\tPreco:{preco}')
    print(f'\tConsumo:{consumo}')
    print(f'\tData:{data}')
    print(f'\tconfiguracao:{configuracao}')
    print(f'\tNota:{nota}')
    for valor,teste in configuracao.items():
        print(f'\t{valor}:{teste}')

dados_computador(1.99,'280w','10','11','12',valor_1='teste_1',valor_2='teste_2',valor_3='3')


def aplicar_desconto(produtos: dict ,desconto:int):
    resultado = {}
    for produto,valor in produtos.items():
        valor_descontado = valor*(1-desconto/100)
        resultado.setdefault(produto,valor_descontado)
    return resultado


lista_de_valores = {
    'produto1':100,
    'produto2':200,
    'produto3':300,
}
lista_com_desconto= aplicar_desconto(lista_de_valores,10)
#print(f"\tsem desconto: {lista_de_valores} \n\tcom desconto:{lista_com_desconto}")

 