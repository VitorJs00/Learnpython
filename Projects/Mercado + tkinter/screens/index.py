import tkinter as tk
from tkinter import *
from tkinter import ttk 
import json
dados_json = '../dados.json'
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
JSON_PATH = BASE_DIR.parent / 'dados.json'
CATEGORIA_PATH = BASE_DIR.parent / 'categorias_supermercado.json'
from tkcalendar import DateEntry

class index:
    def __init__(self,window):
        self.window = window
        with open(JSON_PATH,'r',encoding='utf-8') as file:
            self.data = json.load(file)

        with open(CATEGORIA_PATH,'r',encoding='utf-8') as file:
            self.categoria_data = json.load(file)

        self.categorias = []
        self.sub_categorias = []
        self.newProduto = {
            "Id": "",
            "Nome": "",
            "Marca": "",
            "Categoria": [],
            "Validade": ""
        }

        for element in self.categoria_data.keys():
            self.categorias.append(element)

    def get_sub_categorias(self,categoria):
        self.sub_categorias.clear()
        for item,i in zip(self.categoria_data[str(categoria)],range(len(self.categoria_data[str(categoria)]))):
            self.sub_categorias.append(item)

        self.Sub_Categoria_bbx.config(values=self.sub_categorias)
        print('SUB',self.sub_categorias)


    def build_container(self,):
        container_pai = tk.Frame(master=self.window, bg="yellow",height=200)
        container_pai.pack(fill=tk.X)

        self.add_produto(container_pai)
        self.editar_produto(container_pai)
        self.excluir_produto(container_pai)

        

        
    def add_produto(self,parent):
        frame_button =  tk.Frame(parent,height=80)
        frame_button.pack(fill="x")

        tk.Label(
            frame_button,
            text="NOME:"
        ).pack(side="left")
        self.Nome = tk.Entry(
                frame_button,
                borderwidth=1,
                relief="solid",
                width=15,
            )
        self.Nome.pack(side="left",expand=True,anchor='center')

       
        
        tk.Label(
            frame_button,
            text="MARCA:"
        ).pack(side="left")
        self.Marca = tk.Entry(
                frame_button,
                text="MARCA:",
                borderwidth=1,
                relief="solid",
                width=15
            )
        self.Marca.pack(side="left", expand=True,anchor='center')

        tk.Label(
            frame_button,
            text="CATEGORIA:"
        ).pack(side="left")

        self.Categoria = ttk.Combobox(
                frame_button,
                text="CATEGORIA",
                width=15,
                values=self.categorias,
                state="readonly"
            )
        
        self.Categoria.pack(side="left", expand=True,anchor='center')
        self.Categoria.bind("<<ComboboxSelected>>",self.selecionar_opcao)

        tk.Label(
            frame_button,
            text="SUB-CATEGORIA:"
        ).pack(side="left")
        self.Sub_Categoria_bbx = ttk.Combobox(
                frame_button,
                width=15,
                state="readonly"
            )
        self.Sub_Categoria_bbx.pack(side="left", expand=True,anchor='center')
       

        tk.Label(
            frame_button,
            text="VALIDADE:"
        ).pack(side="left")
        self.Validade = DateEntry(
            frame_button,
            width=12,
            background='darkblue',
            foreground='white',
            borderwidth=2,
            date_pattern='dd/mm/yyyy'
        )
        self.Validade.pack(side="left", expand=True,anchor='center')
        
        tk.Button(
            frame_button,text="ADICIONAR\nPRODUTO",
            command=self.acoes_butao

        ).pack(expand=True,anchor='center')


    def selecionar_opcao(self,event):
        # Obtém a opção selecionada na Combobox
        opcao_selecionada = self.Categoria.get()
        print(opcao_selecionada)
        self.get_sub_categorias(opcao_selecionada)
       

    

    def acoes_butao(self,):
        self.newProduto['Nome'] = self.Nome.get()
        self.newProduto['Marca'] = self.Marca.get()
        self.newProduto['Categoria'] = [self.Categoria.get(),self.Sub_Categoria_bbx.get()]
        self.newProduto['Validade'] = self.Validade.get()

        if (
            self.newProduto['Nome'] and self.newProduto['Marca']
            and self.newProduto['Categoria'] and self.newProduto['Validade']
        ):
            print(self.newProduto)

    def excluir_produto(self,parent):
        frame_button =  tk.Frame(parent,height=80)
        frame_button.pack(fill="x")

        tk.Label(
                frame_button,
                text="VALOR EXCLUIR",
                borderwidth=1,
                relief="solid",
                width=15
            ).pack(side="left", fill="x", expand=True)
    def editar_produto(self,parent):
        frame_button =  tk.Frame(parent,height=80)
        frame_button.pack(fill="x")

        tk.Label(
                frame_button,
                text="VALOR EDITAR",
                borderwidth=1,
                relief="solid",
                width=15
            ).pack(side="left", fill="x", expand=True)