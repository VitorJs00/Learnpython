import tkinter as tk
from tkinter import *
from tkinter import ttk 
import json
import random
dados_json = '../dados.json'
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
JSON_PATH = BASE_DIR.parent / 'dados.json'
CATEGORIA_PATH = BASE_DIR.parent / 'categorias_supermercado.json'
from tkcalendar import DateEntry





class index:
    def __init__(self,window):
        self.window = window
        self.largura = int(self.window.winfo_width())
        self.altura = int(self.window.winfo_height())
        

        with open(JSON_PATH,'r',encoding='utf-8') as file:
            self.data = json.load(file)

        with open(CATEGORIA_PATH,'r',encoding='utf-8') as file:
            self.categoria_data = json.load(file)

        self.categorias = []

        self.sub_categorias = []


        self.edit_categorias = []
        self.edit_sub_categorias = []
        
        

        self.newProduto = {
            "Id": "",
            "Nome": "",
            "Marca": "",
            "Categoria": [],
            "Validade": ""
        }

        for element in self.categoria_data.keys():
            self.categorias.append(element)
            self.edit_categorias.append(element)

        self.nome_text = ''    
        self.id_text = ''
        self.marca_text = ''
        self.validade_text = ''
        self.categoria_text = ''



        self.build_container_dados()

    def get_sub_categorias(self,categoria,use_edit=False):
        self.sub_categorias.clear()
        for item,i in zip(self.categoria_data[str(categoria)],range(len(self.categoria_data[str(categoria)]))):
            self.sub_categorias.append(item)

        self.Sub_Categoria_bbx.config(values=self.sub_categorias)

        if use_edit == True:
            self.edit_Sub_Categoria_bbx.config(values=self.sub_categorias)
            



    def edit_get_sub_categorias(self,categoria,use_edit=False):
        self.edit_sub_categorias.clear()
        for item,i in zip(self.categoria_data[str(categoria)],range(len(self.categoria_data[str(categoria)]))):
            self.edit_sub_categorias.append(item)
        self.edit_Sub_Categoria_bbx.config(values=self.edit_sub_categorias)
        

    def build_container(self,):
        self.container_pai = tk.Frame(master=self.window, bg="yellow",height=200)
        self.container_pai.pack(fill=tk.X)

        self.add_produto(self.container_pai)
        self.editar_produto(self.container_pai)
        self.excluir_produto(self.container_pai)
        
    def add_produto(self,parent):
        self.frame_button =  tk.Frame(parent,height=80)
        self.frame_button.pack(fill="x")

        tk.Label(
            self.frame_button,
            text="NOME:"
        ).pack(side="left")
        self.Nome = tk.Entry(
                self.frame_button,
                borderwidth=1,
                relief="solid",
                width=15,
            )
        self.Nome.pack(side="left",expand=True,anchor='center')

       
        
        tk.Label(
            self.frame_button,
            text="MARCA:"
        ).pack(side="left")
        self.Marca = tk.Entry(
                self.frame_button,
                text="MARCA:",
                borderwidth=1,
                relief="solid",
                width=15
            )
        self.Marca.pack(side="left", expand=True,anchor='center')

        tk.Label(
            self.frame_button,
            text="CATEGORIA:"
        ).pack(side="left")

        self.Categoria = ttk.Combobox(
                self.frame_button,
                text="CATEGORIA",
                width=15,
                values=self.categorias,
                state="readonly"
            )
        
        self.Categoria.pack(side="left", expand=True,anchor='center')
        self.Categoria.bind("<<ComboboxSelected>>",self.selecionar_opcao)

        tk.Label(
            self.frame_button,
            text="SUB-CATEGORIA:"
        ).pack(side="left")
        self.Sub_Categoria_bbx = ttk.Combobox(
                self.frame_button,
                width=15,
                state="readonly"
            )
        self.Sub_Categoria_bbx.pack(side="left", expand=True,anchor='center')
       

        tk.Label(
            self.frame_button,
            text="VALIDADE:"
        ).pack(side="left")
        self.Validade = DateEntry(
            self.frame_button,
            width=12,
            background='darkblue',
            foreground='white',
            borderwidth=2,
            date_pattern='dd/mm/yyyy'
        )
        self.Validade.pack(side="left", expand=True,anchor='center')
        
        tk.Button(
            self.frame_button,text="ADICIONAR\nPRODUTO",
            command=self.create_product

        ).pack(expand=True,anchor='center')


    def selecionar_opcao(self,event,use_edit=False):
        # Obtém a opção selecionada na Combobox
        if use_edit:
           opcao_selecionada = self.edit_Categoria.get()
           self.edit_get_sub_categorias(opcao_selecionada,use_edit) 

          
        else:
            
            opcao_selecionada = self.Categoria.get()
            self.get_sub_categorias(opcao_selecionada,use_edit)
     
    def newProduto_def(self,newProduto_data):

        with open(JSON_PATH, 'r',encoding='utf-8') as file:
            data = list(json.load(file))

        new_produto = newProduto_data
        data.append(new_produto)
        
        with open(JSON_PATH, 'w',encoding='utf-8') as file:
            json.dump(data,file,ensure_ascii=False)
  
    def gerar_id(self,):
            text = "ABCDEFG12345678"
            ids_gerados = [] 
            with open(JSON_PATH,'r',encoding='utf-8') as file:
                data = json.load(file)
            
            for element in data:
                ids_gerados.append(element['Id'])

            
            while True:
                novo_id = ''.join(random.choice(text) for _ in range(5))
                if novo_id not in ids_gerados:
                    ids_gerados.append(novo_id)  
                    return novo_id

    def create_product(self,):
        self.newProduto['Nome'] = self.Nome.get()
        self.newProduto['Marca'] = self.Marca.get()
        self.newProduto['Categoria'] = [self.Categoria.get(),self.Sub_Categoria_bbx.get()]
        self.newProduto['Validade'] = self.Validade.get()
        self.newProduto["Id"] = self.gerar_id()

        if (
            self.newProduto['Nome'] and self.newProduto['Marca']
            and self.newProduto['Categoria'] and self.newProduto['Validade']
        ):
            self.newProduto_def(self.newProduto)
            self.container_dados.destroy()
            self.build_container_dados()
            
            

        else:
            popup = tk.Tk()
            popup.title("ALERTA")

            largura = 300
            altura = 150

            popup.update_idletasks()

            x = (popup.winfo_screenwidth() // 2) - (largura // 2)
            y = (popup.winfo_screenheight() // 2) - (altura // 2)

            Label(popup,text="INSIRA TODOS DADOS DO PRODUTO",bg="#FF5E00",height=30).pack(anchor="center",fill=tk.BOTH)
            popup.geometry(f"{largura}x{altura}+{x}+{y}")


    def edit_product(self,Id):
        print(self.Nome_edit.get())
        print(self.edit_marca.get())

        with open(JSON_PATH, 'r',encoding='utf-8') as file:
            data = list(json.load(file))
        for element,i in zip(data,range(len(data))):
            if element["Id"] == Id:
                data[i]["Nome"] = self.Nome_edit.get()
                data[i]["Marca"] = self.edit_marca.get()
                data[i]["Categoria"] = [self.edit_Categoria.get(),self.edit_Sub_Categoria_bbx.get() ]
                data[i]["Validade"] = self.Validade_edit.get()
        
        
        
        

        if (
            data[i]["Nome"] or data[i]["Marca"] or data[i]["Categoria"]  or data[i]["Validade"] 
            
        ):
            with open(JSON_PATH, 'w',encoding='utf-8') as file:
                json.dump(data,file,ensure_ascii=False)
            
            with open(JSON_PATH, 'r',encoding='utf-8') as file:
                self.data = list(json.load(file))

            self.container_pai.destroy()
            self.container_dados.destroy()
            self.build_container()
            self.build_container_dados()
            
            


        else:
            popup = tk.Tk()
            popup.title("ALERTA")

            largura = 300
            altura = 150

            popup.update_idletasks()

            x = (popup.winfo_screenwidth() // 2) - (largura // 2)
            y = (popup.winfo_screenheight() // 2) - (altura // 2)

            Label(popup,text="FACA AS  MODIFICACOES DO PRODUTO\n OU SELECIONE UMA LINHA",bg="#FF5E00",height=30).pack(anchor="center",fill=tk.BOTH)
            popup.geometry(f"{largura}x{altura}+{x}+{y}")

        
        

    def build_container_dados(self,):
        with open(JSON_PATH,'r',encoding='utf-8') as file:
            self.data = json.load(file)

        self.container_dados = Frame(self.window,bg="#2902B6",height=200,)
        self.container_dados.pack(fill=tk.BOTH, expand=True,side='bottom')
        
        Colunas = tk.Frame(self.container_dados,bg="#C91AC0")
        Colunas.pack(fill="x")

        tk.Label(
                Colunas,
                text="N",
                borderwidth=1,
                relief="solid",
                width=1
            ).pack(side="left", fill="x", expand=True)
        
        tk.Label(
                Colunas,
                text="ID",
                borderwidth=1,
                relief="solid",
                width=15
            ).pack(side="left", fill="x", expand=True)
        tk.Label(
                Colunas,
                text="Nome",
                borderwidth=1,
                relief="solid",
                width=15
            ).pack(side="left", fill="x", expand=True)
        tk.Label(
                Colunas,
                text="Marca",
                borderwidth=1,
                relief="solid",
                width=15
            ).pack(side="left", fill="x", expand=True)
        tk.Label(
                Colunas,
                text="Categorias",
                borderwidth=1,
                relief="solid",
                width=15
            ).pack(side="left", fill="x", expand=True)      
        tk.Label(
                Colunas,
                text="Validade",
                borderwidth=1,
                relief="solid",
                width=15
            ).pack(side="left", fill="x", expand=True)

        for element,i in zip(self.data,range(len(self.data))):
            
            self.criar_linha(self.container_dados,element,i)
            
    def criar_linha(self,parent, valores,i):
        
        frame_linha = tk.Frame(parent)
        frame_linha.pack(fill="x")
        
    
        coluna_num = tk.Label(
           frame_linha,
                text=i,
                borderwidth=1,
                relief="solid",
                width=1,
                bg='red'
        )
        coluna_num.pack(side="left", fill="x", expand=True)
        

        for valor in valores:
            linha_dado= tk.Label(
                frame_linha,
                text=valores[valor],
                borderwidth=1,
                relief="solid",
                width=15,
                bg='yellow',
                
            )
            linha_dado.pack(side="left", fill="x", expand=True)
            linha_dado.config( borderwidth=0,relief=None)

            linha_dado.bind("<Button-1>", lambda e: self.linha_select(valores,linha=frame_linha))

        


    def linha_select(self,valores,linha):
        
        if hasattr(self, 'linha_anterior') and self.linha_anterior:
            print('select',self.id_text)

            self.linha_anterior.config(borderwidth=0, relief="flat")

        

        self.Nome_edit.delete(0,END)
        self.edit_marca.delete(0,END)
        
        self.Nome_edit.insert(0,string=valores['Nome'])
        self.edit_marca.insert(0,string=valores["Marca"])
        linha.config( borderwidth=2,relief='solid')
        #CORRCAO ERRO SELF.MARCA TAMBEM EXIBINDO TEXTO
        self.Marca.delete(0,END)

        #BORDER NA LINHA
        
        self.linha_anterior = linha
        self.id_text = valores["Id"]

        

    def excluir_produto(self,parent):
        self.frame_button =  tk.Frame(parent,height=80)
        self.frame_button.pack(fill="x")

        tk.Label(
                self.frame_button,
                text="VALOR EXCLUIR",
                borderwidth=1,
                relief="solid",
                width=15
            ).pack(side="left", fill="x", expand=True)
    
    def editar_produto(self,parent):
        self.frame_button_edit =  tk.Frame(parent,height=80)
        self.frame_button_edit.pack(fill="x")

        tk.Label(
            self.frame_button_edit,
            text="NOME:",

        ).pack(side="left")
        self.Nome_edit = tk.Entry(
                self.frame_button_edit,
                borderwidth=1,
                relief="solid",
                width=15,
                
            )
        #self.Nome_edit.insert(0, f"{self.nome_text}")
        self.Nome_edit.pack(side="left",expand=True,anchor='center')
        


        tk.Label(
            self.frame_button_edit,
            text="MARCA: "
        ).pack(side="left")
        self.edit_marca= tk.Entry(
                self.frame_button_edit,
                text="MARCA: ",
                borderwidth=1,
                relief="solid",
                width=15
            )
        self.edit_marca.pack(side="left", expand=True,anchor='center')

        tk.Label(
            self.frame_button_edit,
            text="CATEGORIA:"
        ).pack(side="left")

        self.edit_Categoria = ttk.Combobox(
                self.frame_button_edit,
                text="CATEGORIA ",
                width=15,
                values=self.edit_categorias,
                state="readonly"
            )
        
        self.edit_Categoria.pack(side="left", expand=True,anchor='center')
        self.edit_Categoria.bind("<<ComboboxSelected>>",lambda e: self.selecionar_opcao(use_edit=True,event=None))

        tk.Label(
            self.frame_button_edit,
            text="SUB-CATEGORIA:"
        ).pack(side="left")
        self.edit_Sub_Categoria_bbx = ttk.Combobox(
                self.frame_button_edit,
                width=15,
                state="readonly",
                
            )
        self.edit_Sub_Categoria_bbx.pack(side="left", expand=True,anchor='center')
       

        tk.Label(
            self.frame_button_edit,
            text="VALIDADE:"
        ).pack(side="left")
        self.Validade_edit = DateEntry(
            self.frame_button_edit,
            width=12,
            #background='darkblue',
            #foreground='white',
            borderwidth=2,
            date_pattern='dd/mm/yyyy'
        )
        self.Validade_edit.pack(side="left", expand=True,anchor='center')
        
        
        tk.Button(
            self.frame_button_edit,text="EDITAR\nPRODUTO",
            command=lambda:self.edit_product(self.id_text)

        ).pack(expand=True,anchor='center')