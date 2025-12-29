novo_text = '\n\ntexto appendidio'
Arquivo = open(
    'C:\\Users\\Tatiane\\Documents\\CODIGOS\\python\\pyBasic\\Learnpython\\manipulacao_arquivos\\texto.txt',
    'a'
)
#Arquivo.write('OLA BANDOLEIRO')
#txt = Arquivo.read()
#print(txt)
Arquivo.write(novo_text)
Arquivo.close()

Arquivo_binario = open(
    'C:\\Users\\Tatiane\\Documents\\CODIGOS\\python\\pyBasic\\Learnpython\\manipulacao_arquivos\\logo.png',
    'rb'
)

Arquivo_binario_saida = open(
    'C:\\Users\\Tatiane\\Documents\\CODIGOS\\python\\pyBasic\\Learnpython\\manipulacao_arquivos\\logo_saida.png',
    'wb'
)
ler_arquivo = Arquivo_binario.read()
print(ler_arquivo)

montar_img = Arquivo_binario_saida.write(ler_arquivo)

Arquivo_binario.close()
Arquivo_binario_saida.close()