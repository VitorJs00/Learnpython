import random
class Desktop:
    def __init__(self,modelo,processador,armazenamento,placa_de_video,fonte,):
        self.modelo = modelo
        self.processador = processador
        self.armazenamento = armazenamento
        self.placa_de_video = placa_de_video
        self.fonte = fonte

    def get_info_desktop(self, ):
        print(f"{self.modelo:}\n{self.processador:}\n{self.armazenamento:}\n{self.placa_de_video:}\n{self.fonte:}")

    def preco_desktop(self,processador,placa_de_video):
        raise NotImplementedError
    

class Notebook(Desktop):
    def __init__(self, modelo, processador, armazenamento, placa_de_video, fonte):
        super().__init__(modelo, processador, armazenamento, placa_de_video, fonte)

    def preco_desktop(self, ano, dolar):
        print(f"Preco:{random.randint(ano,ano+dolar)}")




desktop_1 = Notebook('acer nitro 5',"ryzen 5600X",480,"RTX 4090",1000)
desktop_1.get_info_desktop()
desktop_1.preco_desktop(ano=2026,dolar=5)