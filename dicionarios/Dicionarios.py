nomes= ['travis','scott']
idades = [23,19]
dc_1 = {
    'nome':'',
    'idade':''
}


for nome,idade  in zip(nomes, idades):
    dc_1['nome']=nome
    dc_1['idade']=idade
    dc_1['novo'] = '?'
    print(dc_1)
    
txt = dc_1.get('altura', None)
print(txt)