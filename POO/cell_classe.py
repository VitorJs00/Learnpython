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
    
}
class Computador:
    def __init__(self, configuracao,preco,consumo):
        self.configuracao = configuracao
        self.preco = preco
        self.consumo = consumo

    def get_info(self,chave):
        try:
            parametro = self.configuracao[chave]
            mensagem = f"-----INFO-----\ndados:\n\t{chave} \t {parametro}"
            return mensagem
        
        except:
            if chave == 'preço': return f"-----INFO-----\ndados:\n\t{chave} \t {self.preco}"
            elif chave == 'consumo': return f"-----INFO-----\ndados:\n\t{chave} \t {self.consumo}"
            else: return f"A entrada:{chave} é invalida"

computador = Computador(computador['configuracao'],computador['preço'],computador['consumo'])
info = computador.get_info('consumo')
print(info)