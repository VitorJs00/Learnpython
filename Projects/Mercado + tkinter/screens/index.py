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
            
    def edit_get_sub_categorias(self, categoria, use_edit=False):
        """Atualiza subcategorias para edição"""
        if not categoria:
            return
        
        self.edit_sub_categorias.clear()
        
        # Verificar se a categoria existe nos dados
        if categoria in self.categoria_data:
            for item in self.categoria_data[str(categoria)]:
                self.edit_sub_categorias.append(item)
        
        # Atualizar combobox
        if use_edit:
            self.edit_Sub_Categoria_bbx.config(values=self.edit_sub_categorias)
            # Manter a seleção atual se existir
            current_value = self.edit_Sub_Categoria_bbx.get()
            if current_value and current_value in self.edit_sub_categorias:
                self.edit_Sub_Categoria_bbx.set(current_value)
            else:
                self.edit_Sub_Categoria_bbx.set('')

    def build_container(self,):
        self.container_pai = tk.Frame(master=self.window, bg="yellow",height=200)
        self.container_pai.pack(fill=tk.X)

        self.add_produto(self.container_pai)
        self.editar_produto(self.container_pai)
        self.excluir_produto(self.container_pai)
        self.pesquisar_produto(self.container_pai)


    def pesquisar_produto(self,parent):
        
        self.pesquisa_frame = Frame(parent,height=40,background='yellow')
        self.pesquisa_frame.pack(fill='x')


        self.botao_pesquisar = Button(self.pesquisa_frame,anchor=CENTER,text='PESQUISAR',command=self.build_pesquisa_result)
        self.botao_pesquisar.pack(side=RIGHT)


        self.value_pesquisa = Entry(self.pesquisa_frame,background='white',width=90)
        self.value_pesquisa.pack(side=LEFT,fill='x')

        self.entrada = self.value_pesquisa.get()
        
        

    def build_pesquisa_result(self,):
        self.entrada = self.value_pesquisa.get()
        if hasattr(self, 'container_dados'):
            print('destruido')
            self.container_dados.destroy()
        
        
        if self.entrada =='':
            print('construido')
        # Reconstruir apenas os dados
            self.build_container_dados()
        
        else:
            
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
                if self.value_pesquisa.get().lower() in element["Nome"].lower():
                    self.criar_linha(self.container_dados,element,i)


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

    def edit_product(self, Id):
        #print(f"Editando ID: {Id}")
        #print(f"Nome edit: {self.Nome_edit.get()}")
        #print(f"Marca edit: {self.edit_marca.get()}")
        
        # Verificar se há um ID válido selecionado
        if not Id or Id == "" or Id is None:
            self.mostrar_popup("Selecione um produto para editar!")
            return
        
        # Ler dados atuais
        with open(JSON_PATH, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Encontrar e atualizar o produto
        produto_encontrado = False
        for i, element in enumerate(data):
            if element.get("Id") == Id:
                #print(f"Encontrado produto: {element}")
                
                # Atualizar apenas campos que foram modificados
                novo_nome = self.Nome_edit.get()
                if novo_nome and novo_nome != element["Nome"]:
                    data[i]["Nome"] = novo_nome
                
                nova_marca = self.edit_marca.get()
                if nova_marca and nova_marca != element["Marca"]:
                    data[i]["Marca"] = nova_marca
                
                nova_categoria = [self.edit_Categoria.get(), self.edit_Sub_Categoria_bbx.get()]
                if any(nova_categoria) and nova_categoria != element["Categoria"]:
                    data[i]["Categoria"] = nova_categoria
                
                nova_validade = self.Validade_edit.get()
                if nova_validade and nova_validade != element["Validade"]:
                    data[i]["Validade"] = nova_validade
                
                produto_encontrado = True
                break
        
        if not produto_encontrado:
            self.mostrar_popup("Produto não encontrado!")
            return
        
        # Salvar no arquivo
        with open(JSON_PATH, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        
        #print("Dados salvos no JSON")
        
        # Atualizar dados na memória
        with open(JSON_PATH, 'r', encoding='utf-8') as file:
            self.data = json.load(file)
        
        # Atualizar visualização SEM destruir tudo
        self.atualizar_visualizacao()
        
        # Limpar campos de edição
        self.limpar_campos_edicao()

    def delete_product(self,Id):
        # Ler dados atuais
        with open(JSON_PATH, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Encontrar e atualizar o produto
        produto_encontrado = False
        for i, element in enumerate(data):
            if element.get("Id") == Id:
                #print(f"Encontrado produto: {element}")
                
                del data[i]
                produto_encontrado = True
                break
        
        if not produto_encontrado:
            self.mostrar_popup("Produto não encontrado!")
            return
        
        # Salvar no arquivo
        with open(JSON_PATH, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        
        #print("Dados salvos no JSON")
        
        # Atualizar dados na memória
        with open(JSON_PATH, 'r', encoding='utf-8') as file:
            self.data = json.load(file)
        
        # Atualizar visualização SEM destruir tudo
        self.atualizar_visualizacao()
        
        # Limpar campos de edição
        self.limpar_campos_edicao()

    def atualizar_visualizacao(self):
        """Atualiza apenas a visualização dos dados"""
        # Destruir apenas o container de dados
        if hasattr(self, 'container_dados'):
            self.container_dados.destroy()
        
        # Reconstruir apenas os dados
        self.build_container_dados()
        
        # Não destruir o container pai (com botões de edição)
        # para manter os valores nos campos

    def limpar_campos_edicao(self):
        """Limpa os campos de edição após salvar"""
        self.Nome_edit.delete(0, END)
        self.edit_marca.delete(0, END)
        self.edit_Categoria.set('')
        self.edit_Sub_Categoria_bbx.set('')
        self.Validade_edit.delete(0, END)
        self.Validade_edit.set_date(None)
        self.id_text = None

    def mostrar_popup(self, mensagem):
        """Mostra um popup com mensagem"""
        popup = tk.Toplevel(self.window)
        popup.title("ALERTA")
        
        largura = 400
        altura = 120
        
        popup.update_idletasks()
        
        x = (popup.winfo_screenwidth() // 2) - (largura // 2)
        y = (popup.winfo_screenheight() // 2) - (altura // 2)
        
        tk.Label(popup, text=mensagem, bg="#FF5E00", 
                font=("Arial", 10), wraplength=350).pack(pady=20, padx=10)
        
        tk.Button(popup, text="OK", command=popup.destroy).pack(pady=10)
        
        popup.geometry(f"{largura}x{altura}+{x}+{y}")
        popup.transient(self.window)  # Torna a janela modal
        popup.grab_set()

    def build_container_dados(self,pesquisa=False):
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

    def linha_select(self, valores, linha):
        # Salvar a linha anterior
        if hasattr(self, 'linha_anterior') and self.linha_anterior:
            try:
                self.linha_anterior.config(borderwidth=0, relief="flat", bg='SystemButtonFace')
            except:
                pass
        
        # Aplicar borda na nova linha
        try:
            linha.config(borderwidth=2, relief='solid', bg='lightblue')
        except:
            pass
        
        # Atualizar campos de edição
        self.Nome_edit.delete(0, END)
        self.edit_marca.delete(0, END)
        self.nome_del.config(text='')
        self.Id_del.config(text='')
        self.Marca_del.config(text='')
        self.Categorias_del.config(text='')
        self.validade_del.config(text='')

        # Preencher com valores da linha selecionada
        self.Nome_edit.insert(0, string=valores.get('Nome', ''))
        self.edit_marca.insert(0, string=valores.get("Marca", ""))

        self.nome_del.config(text=valores.get("Nome", ""))
        self.Id_del.config(text=valores.get("Id", ""))
        self.Marca_del.config(text=valores.get("Marca", ""))
        self.Categorias_del.config(text=valores.get("Categoria", ""))
        self.validade_del.config(text=valores.get("Validade", ""))




        # Preencher categoria se existir
        categorias = valores.get("Categoria", [])
        if categorias and len(categorias) >= 2:
            self.edit_Categoria.set(categorias[0])
            self.edit_Sub_Categoria_bbx.set(categorias[1])
            # Atualizar subcategorias
            self.edit_get_sub_categorias(categorias[0], use_edit=True)
        
        # Preencher validade se existir
        validade = valores.get("Validade", "")
        if validade:
            try:
                # Converter string de data para o formato do DateEntry
                if '/' in validade:
                    dia, mes, ano = validade.split('/')
                    data_formatada = f"{ano}-{mes}-{dia}"
                    self.Validade_edit.set_date(data_formatada)
            except:
                pass
        
        # Salvar referências
        self.linha_anterior = linha
        self.id_text = valores.get("Id", "")
        
        #print(f"Linha selecionada - ID: {self.id_text}")

    def excluir_produto(self,parent):
        self.frame_button_del =  tk.Frame(parent,height=80)
        self.frame_button_del.pack(fill="x")
       
        tk.Button(
            self.frame_button_del,text="   EXCLUIR\nPRODUTO   ",
            command=self.excluir_produto_selecionado,anchor='center'

        ).pack(expand=True,side=RIGHT,anchor='s')

        tk.Label(
                self.frame_button_del,
                
                borderwidth=1,
                relief="solid",
                width=1,
                padx=30
            ).pack( fill="x", expand=True,side=LEFT)
        
        self.Id_del = tk.Label(
                self.frame_button_del,
                text="ID:",
                borderwidth=1,
                relief="solid",
                width=23
            )
        self.Id_del.pack( fill="x", expand=True,side=LEFT)
        self.nome_del = tk.Label(
                self.frame_button_del,
                text="Nome",
                borderwidth=1,
                relief="solid",
                width=23
            )
        self.nome_del.pack( fill="x", expand=True,side=LEFT)
        self.Marca_del = tk.Label(
                self.frame_button_del,
                text="Marca",
                borderwidth=1,
                relief="solid",
                width=23
            )
        self.Marca_del.pack( fill="x", expand=True,side=LEFT)

        self.Categorias_del = tk.Label(
                self.frame_button_del,
                text="Categoria",
                borderwidth=1,
                relief="solid",
                width=23
            )
        self.Categorias_del.pack( fill="x", expand=True,side=LEFT)
        
        self.validade_del = tk.Label(
                self.frame_button_del,
                text="Validade",
                borderwidth=1,
                relief="solid",
                width=23
            )
        self.validade_del.pack( fill="x", expand=True,side=LEFT)      
    
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
            self.frame_button_edit,text="   EDITAR\nPRODUTO   ",
            command=self.editar_produto_selecionado

        ).pack(expand=True,anchor='center')

    def editar_produto_selecionado(self):
        """Wrapper para editar produto com validação"""
        if not self.id_text or self.id_text == "":
            self.mostrar_popup("Selecione um produto para editar!")
            return
        
        # Verificar se há alterações
        if (not self.Nome_edit.get() and 
            not self.edit_marca.get() and 
            not self.edit_Categoria.get()):
            self.mostrar_popup("Faça modificações antes de salvar!")
            return
        
        self.edit_product(self.id_text)

    def excluir_produto_selecionado(self):
        if not self.id_text or self.id_text == "":
            self.mostrar_popup("Selecione um produto para editar!")
            return     
        self.delete_product(self.id_text)