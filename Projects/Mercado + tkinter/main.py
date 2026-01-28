import tkinter as tk
from screens import index

class App():
    def __init__(self,window):
        self.window = window
        self.window.geometry("900x800")
        self.index = index.index(self.window) 
    def run_app(self,):
        self.index.build_container()   
        window.mainloop()

        


if __name__ == '__main__':
    window = tk.Tk()
    
    app = App(window) 
    app.run_app()

