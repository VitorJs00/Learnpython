import random
import json
class Produto:
    def __init__(self,Nome,Marca, Categoria, Validade):
        self.Nome = Nome
        self.Marca = Marca
        self.Id = self.gerar_id()
        self.Categoria = Categoria
        self.Validade = Validade
        pass
    

    
    def criar_produto(self,):
        produto = {
            "Nome":self.Nome,
            "Marca":self.Marca,
            "Id":self.Id,
            "Categoria":self.Categoria,
            "Validade":self.Validade
        }
        return produto

    def gerar_id(self):
        text = "ABCDEFG12345678"
        ids_gerados = [] 
        with open('dados.json','r') as file:
           data = json.load(file)
        
        for element in data:
            ids_gerados.append(element['Id'])

        print(ids_gerados)
        while True:
            novo_id = ''.join(random.choice(text) for _ in range(5))
            if novo_id not in ids_gerados:
                ids_gerados.append(novo_id)  
                return novo_id
       

    def get_categorias():
        categorias = list()

        with open('categorias_supermercado.json','r',encoding='utf-8') as file:
            data = dict(json.load(file))
        for element in data.keys():
            categorias.append(element)

        

        return categorias,data
