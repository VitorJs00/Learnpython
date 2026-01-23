VALOR_PEDAGIO_CARRO = 3
VALOR_PEDAGIO_MOTO = 2
VALOR_POR_KM_CARRO = 5
VALOR_POR_KM_MOTO = 3

class  Automovel:
    def __init__(self, montadora,modelo,alugado):
        self.montadora = montadora
        self.modelo = modelo
        self.alugado = alugado
        self.valor_fatura = 0
        self.nome_cliente = ""
        
    def alugar(self,nome_cliente):
        self.alugado = True
        self.nome_cliente = nome_cliente
        print(f'o {self.montadora}:{self.modelo} foi alugado por {self.nome_cliente}')
    
    def devolver_automovel(self):
        self.alugado = False
        self.nome_cliente = ''
        print(f'o {self.montadora}:{self.modelo} foi DEVOLVIDO por {self.nome_cliente}')


    def gerar_valor_fatura(self,numero_pedagios, km_rodados):
        raise NotImplementedError


class Carro(Automovel):
    def __init__(self, montadora, modelo, alugado):
        super().__init__(montadora, modelo,alugado)
        print(f'AUTOMOVEL ADQUIRIDO: CARRO')


    def gerar_valor_fatura(self,numero_pedagios, km_rodados):
        self.valor_fatura = (numero_pedagios*VALOR_PEDAGIO_CARRO + VALOR_POR_KM_CARRO*km_rodados)
        print(f'FATURA {self.montadora}:{self.modelo} É DE :{self.valor_fatura}')


class Moto(Automovel):
    def __init__(self, montadora, modelo, alugado):
        super().__init__(montadora, modelo, alugado)
        print(f'AUTOMOVEL ADQUIRIDO: MOTO')

    def gerar_valor_fatura(self,numero_pedagios, km_rodados):
        self.valor_fatura = (numero_pedagios*VALOR_PEDAGIO_MOTO + VALOR_POR_KM_MOTO*km_rodados)
        print(f'FATURA {self.montadora}:{self.modelo} É DE :{self.valor_fatura}')


def mostrar_fatura(automovel):
    print(f'{automovel.montadora}:{automovel.modelo}-ALUGADO:{automovel.nome_cliente}-VALOR:{automovel.valor_fatura}')


fiesta = Carro('Ford','Fiesta',False)
fiesta.alugar('JOAO')
fiesta.devolver_automovel()
fiesta.gerar_valor_fatura(2,20)
mostrar_fatura(fiesta)