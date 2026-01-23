carro_1 = {
    'tempo':'15',
    'distancia':'60'
}

carro_2 = {
    'tempo':'18',
    'distancia':'50'
}

def comparar_carros(carro_1,carro_2):
    tempo_1 = float(carro_1['tempo'])
    tempo_2 = float(carro_2['tempo'])
    distancia_1 = float(carro_1['distancia'])
    distancia_2 = float(carro_2['distancia'])
    result_1 = distancia_1/tempo_1
    result_2 = distancia_2/tempo_2
    return f'O mais veloz é {'Carro1' if result_1>result_2 else 'carro2'}'


aluno_1 = [6,4,5]

def modia_mediana(aluno):
    aluno.sort()
    tamanho = len(aluno)
    media = sum(aluno)/tamanho
    if tamanho%2 == 0:
        index = (tamanho - 2) // 2
        mediana = (aluno[index] + aluno[index+1])/2
    else:
        mediana = aluno[int(tamanho//2)]
    return media,mediana


#media,mediana = modia_mediana(aluno_1)
#print(f'a media: {media:.2f} e a mediana:{mediana}')

def funcao_multiplo_args(arg_1,*args):
    print(f'arg1 :{arg_1}')
    print(f'*arg:{args}')

