import tkinter as tk

from cadastro import SistemaCadastroApp
from tarefas import TarefaApp


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema com Alternância de Telas")
        self.geometry("2000x2000")

        menu = tk.Frame(self, bg="#f0f0f0")
        menu.pack(side="top", fill="x")

        btn_pessoas = tk.Button(menu, text="Cadastro de Pessoas", command=self.mostrar_pessoas)
        btn_tarefas = tk.Button(menu, text="Cadastro de Tarefas", command=self.mostrar_tarefas)
        btn_pessoas.pack(side="left", padx=10, pady=5)
        btn_tarefas.pack(side="left", padx=20, pady=5)

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.tela_pessoas = SistemaCadastroApp(self.container)
        self.tela_tarefas = TarefaApp(self.container)

        for tela in (self.tela_pessoas, self.tela_tarefas):
            tela.grid(row=0, column=0, sticky="nsew")

        self.mostrar_pessoas()

    def mostrar_pessoas(self):
        self.tela_pessoas.tkraise()

    def mostrar_tarefas(self):
        self.tela_tarefas.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()

