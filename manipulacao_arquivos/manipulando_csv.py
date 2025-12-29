lista_dados = []
with open("./cadastro.csv",'r') as dados_entrada:
    linhas = dados_entrada.readlines()[1:]
    for linha in linhas:
        dados = linha.split(',')
        email = dados[3].replace('\n','')
        lista_dados.append(f'{dados[1]} {dados[2]}, {dados[3]}')

with open('./cadastro_saida.csv','w') as dados_saida:
    for dado in lista_dados:
        dados_saida.write(dado)