from components.edit_dados import Editar,get_opcoes,get_info
computador = {

    'configuracao':{
        'placa_de_video':{
            'nome':'RTX 3090',
            'fabricante':'NVIDIA',
            'ano':'2023',

        },
        'processador':{
            'nome':'Ryzen 5600X',
            'fabricante':'AMD',
            'ano':'2017',

        },
        'quantidade_fan':3,
        'ram':{
            'total_capacidade':'16gb',
            'mhz':'2666mhz'
        },
        'cooler':'Whater Plus',
        'fonte':{
            'fabricante':'Turbilhao PRO',
            'ano':'2019',
            'potencia':'700w'
        },
        'armazenamento':[
            {
                'fabricante':'YYYYYY',
                'ano':'YYYY', 
                'capacidade':'480gb',
                'tipo':'ssd'
            },
            {   
                'fabricante':'KKKKKK',
                'ano':'KKKK', 
                'capacidade':'1t',
                'tipo':'nvme'
            }
        ]
    },
    'preço':3999.00,
    'consumo':'280w',
    'data_de_compra':'23-05-2021'
}

try:
    opcoes = get_opcoes(computador)
    computador_editado = Editar(computador,opcoes)
    print(get_info(computador_editado,'ram'))
except:
    print('erro ao carregar opcoes')