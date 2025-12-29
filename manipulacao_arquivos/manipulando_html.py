import re
saida_json = {
    "titulo":{
        "ICON":"",
        "LINK":""
    }
}


lista_teste = []

with open('./marcadores_26_12_2025.html','r',encoding='utf-8') as entrada:
    arquivo_context = entrada.read()
    lista_teste.append(arquivo_context)


padrao_titulos = r'<DT><A\b[^>]*>(.*?)</A>'
padrao_links = r'HREF=[^>]* ADD_DATE'
padrao_icons = r'"data:image[^>]*">'



titulos = re.findall(padrao_titulos, arquivo_context, flags=re.DOTALL | re.IGNORECASE)
links = re.findall(padrao_links, arquivo_context, flags=re.DOTALL | re.IGNORECASE)
icons = re.findall(padrao_icons,arquivo_context,flags=re.DOTALL |re.IGNORECASE)


with open('./marcadores_26_12_2025.json','w',encoding='utf-8',) as saida:
    saida.write('{\n')
    for titulo,icon,link in zip(titulos,icons,links):
        link = link.replace('HREF=','')
        link =link.replace(' ADD_DATE','')
        icon = icon.replace('>','')
        dados = f'{{"ICON":{icon},"LINK":{link}}},'
        linha = f'"{titulo}":{str(dados)}\n'
        
        saida.write(format(linha))
    saida.write('}\n')
    