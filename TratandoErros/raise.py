cadastro = [
    'Ana,28,Ads',
    'Beatriz,23,Ecomp',
    'Cris,21a,a',
    'Diana,22,EngA',

]
def processar_dados(cadastros):
    for cadastro in cadastros:
        dados = cadastro.split(',')
        if len(dados)!=3:
            raise ValueError('FORMATO CSV ERRADO')
        nome=dados[0]
        curso=dados[2]
        try:   
            idade=int(dados[1])
        except:
            raise ValueError('IDADE NO FORMATO ERRADO')
        
        print(f'{nome} tem {idade} Anos e cursa:{curso}')

try:
    processar_dados(cadastro)
except ValueError as e:
    print(f'DEU PAU ERRO:{e}')