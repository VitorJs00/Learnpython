import tkinter as tk
from tkinter import *
import json
dados_json = '../dados.json'
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
JSON_PATH = BASE_DIR.parent / 'dados.json'

class exibir_dados(tk.Tk):
    def __init__(self, window):
        self.window = window
        self.largura = int(self.window.winfo_width())
        self.altura = int(self.window.winfo_height())

        with open(JSON_PATH,'r',encoding='utf-8') as file:
            self.data = json.load(file)

    def build_container(self,):
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
        frame = tk.Frame(parent)
        frame.pack(fill="x")

        tk.Label(
            frame,
                text=i,
                borderwidth=1,
                relief="solid",
                width=1
        ).pack(side="left", fill="x", expand=True)
        

        for valor in valores:
            tk.Label(
                frame,
                text=valores[valor],
                borderwidth=1,
                relief="solid",
                width=15
            ).pack(side="left", fill="x", expand=True)

    
    