import requests
import json
teste = requests.get('http://localhost:25600/api/v1/series/latest',auth=('guildagodlevelup@gmail.com', 'tatiane1'))
json_teste=teste.json()
#print(json_teste['content'][0]['name'])

numero_elements = len(json_teste['content'])
series = []
def titulo(element) : return json_teste['content'][element]["metadata"]['title']
def booksCount(element): return json_teste['content'][element]["booksCount"]
def created(elementt): return json_teste['content'][element]["created"]
with open('../dados/hqs.json','w') as saida:
    for element in range(numero_elements):
        series.append(json_teste['content'][element])
    saida.write(json.dumps(series,ensure_ascii=False))

saida_csv = list()
with open('../dados/hqs.csv','w') as saida_csv:
    saida_csv.write('title,numero_livros,criado_em\n')
    for element in range(numero_elements):
        saida_csv.write(f"{titulo(element)},{ booksCount(element)},{created(element)}\n")