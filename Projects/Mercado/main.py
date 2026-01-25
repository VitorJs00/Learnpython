import json
from components import Produto as P
class main:
    def __init__(self,):
        self.rodando=True
        pass
    
    def app(self,):
        while self.rodando:
            
            try:
                comando = int(input(f'{'-'*20}\nADICIONAR:[1]\nEXCLUIR:[2]\nATUALIZAR[3]\nSAIR:[4]\n{'-'*20}'))
                

                if comando == 1:
                    self.criar_produto()
                if comando ==2:
                    self.excluir_produto()

                if comando == 4:
                    self.rodando = False
                    break
            except Exception as e:
                print(f'1 - ENTRADA INVALIDA:{e}')

    def criar_produto(self,):
        try:
            self.Nome = input('NOME DO PRODUTO: ')
            self.Marca= input('MARCA DO PRODUTO: ')
            self.Categoria= self.get_categorias()
            self.Validade = input('INFORME A DATA DE VENCIMENTO DO PRODUTO: ')

        except Exception as e:
            print(f'2 - ENTRADA INVALIDA. ERRO:{e}')
        

        with open('dados.json', 'r',encoding='utf-8') as file:
            data = list(json.load(file))
        new_produto = P.Produto(self.Nome,self.Marca,self.Categoria,self.Validade).criar_produto()
        data.append(new_produto)
        with open('dados.json', 'w',encoding='utf-8') as file:
            json.dump(data,file,ensure_ascii=False)
           
    def get_categorias(self,):
        self.categoria = []
        self.sub_categoria = []
        self.categorias,self.data = P.Produto.get_categorias()
        text_opcoes = f'{'-'*10}ESCOLHA A CATEGORIA DO PRODUTO{'-'*10}\n'
        text_sub_opcoes =  f'{'-'*10}ESCOLHA A SUB-CATEGORIA DO PRODUTO{'-'*10}\n'

        for item,i in zip(self.categorias,range(len(self.categorias))):
            text_opcoes+=f'\t{item}:[{i}]\n'

        escolha = int(input(text_opcoes))
        self.categoria.append(self.categorias[escolha])

        for item,i in zip(self.data[self.categorias[escolha]],range(len(self.categorias[escolha]))):
            text_sub_opcoes+=f'\t{item}:[{i}]\n'
            self.sub_categoria.append(item)


        sub_escolha = int(input(text_sub_opcoes))
        self.categoria.append(self.sub_categoria[sub_escolha])

        return self.categoria
        
    def close_app(self,):
        self.rodando = False

    def excluir_produto(self,):
        try:
            Id = input('INFORME O ID PARA EXCLUIR O PRODUTO')
            with open('dados.json', 'r',encoding='utf-8') as file:
                data = json.load(file)
            for element,i in zip(data,range(len(data))):
                if Id == element['Id']:
                    data.pop(i)
                else:
                    print(f'O PRODUTO COM ID:{Id} NAO EXISTE')
            with open('dados.json', 'w',encoding='utf-8') as file:
                json.dump(data,file,ensure_ascii=False)
        except Exception as e:
            print(f'ERRO:{e}')
            
    def atualizar_produto(self,):
        try:
            Id = input('INFORME O ID PARA EDITAR O PRODUTO')
            with open('dados.json', 'r',encoding='utf-8') as file:
                data = json.load(file)
            for element,i in zip(data,range(len(data))):
                if Id == element['Id']:
                    for opcao in element:
                        if opcao != 'Id' and opcao !='Categoria':

                            escolha = int(input(f'EDITAR:{opcao}? [1]:SIM [2]:NAO          '))
                            if escolha == 1:
                                novo_valor = input(f'INSIRA O NOVO VALOR: ')
                                element.update({opcao:novo_valor})
                                

                            elif escolha==2: continue

                            else: 
                                print(f'entrada invalida')
                                continue
                        elif opcao =='Categoria':
                            escolha = int(input(f'EDITAR:{opcao}? [1]:SIM [2]:NAO          '))
                            if escolha == 1:
                                element.update({opcao:self.get_categorias()})

                else:
                    print(f'O PRODUTO COM ID:{Id} NAO EXISTE')
            with open('dados.json', 'w',encoding='utf-8') as file:
                json.dump(data,file,ensure_ascii=False)
        except Exception as e:
            print(f'ERRO:{e}')

    def visualizar_produtos(self,):
        lista_categorias,data_categorias = P.Produto.get_categorias()
        lista_sub_categorias= []
        with open('dados.json','r') as file:
                data = json.load(file)

        text_opcoes = f'{'-'*10}ESCOLHA A CATEGORIA DO PRODUTO{'-'*10}\n'
        text_sub_opcoes =  f'{'-'*10}ESCOLHA A SUB-CATEGORIA DO PRODUTO{'-'*10}\n'

        for item,i in zip(lista_categorias,range(len(lista_categorias))):
                    for sub_item in data_categorias[item]:           
                        lista_sub_categorias.append(sub_item)
                        
        for sub_item,i in zip(lista_sub_categorias,range(len(lista_sub_categorias))):
            text_sub_opcoes+=f'\t{sub_item}:[{i}]]\n'

        for item,i in zip(lista_categorias,range(len(lista_categorias))):
            text_opcoes+=f'\t{item}:[{i}]\n'

        

        try:
            escolha_filtro = int(input(f'{'-'*20}ESCOLHA O FILTRO{'-'*20}\n\tTODOS PRODUTOS:[1]\n\tCATEGORIA[2]\n\tSUBCATEGORIA[3]\n \t:'))
            if escolha_filtro == 1:
                for item,i in zip(data,range(len(data))):
                    print(f'Item {i}:{item}')
            
            elif escolha_filtro ==2:
                escolha = int(input(text_opcoes))
                for item,i in zip(data,range(len(data))):
                    if lista_categorias[escolha] in item["Categoria"] :
                        print(f'Item {i}:{item}')


            elif escolha_filtro == 3:
                escolha = int(input(text_opcoes))
                sub_escolha = int(input(text_sub_opcoes))
                
                for item,i in zip(data,range(len(data))):
                    if [lista_categorias[escolha],lista_sub_categorias[sub_escolha]] == item["Categoria"]:
                        print(f'Item {i}:{item}')




        except Exception as e:
            print(f'{e}')


if __name__ == '__main__':
    app = main()
    app.visualizar_produtos()