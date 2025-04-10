import tkinter as tk

from pymongo import MongoClient

from ctypes import windll

from tkinter import ttk, messagebox

from bson.objectid import ObjectId

from bson import ObjectId

class TarefaApp(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(bg="#f0f0f0")
        tk.Label(self, text="Cadastro de Tarefas").pack()

        self.janela = janela

        self.cliente = MongoClient("mongodb://localhost:27017")

        self.bd = self.cliente["cadastroUsuarios"]

        self.colecao = self.bd["Tarefas"]

        estilo = ttk.Style()

        estilo.theme_use('default')

        estilo.configure("Treeview",
                         background="#ffffff",
                         foreground="black",
                         rowheight=25,
                         fielbackground="#ffffff",
                         font=("Arial", 11))

        estilo.configure("Treeview.Heading",
                         font=("Arial", 12, "bold"))

        estilo.map("Treeview",

                   background=[("selected", "black")],
                   foreground=[("selected", "white")])

        quadroEntrada = tk.Frame(self,
                                 bg="#f0f0f0")

        quadroEntrada.pack(pady=10,
                           padx=10,
                           fill="x")

        rotuloTitulo = tk.Label(quadroEntrada,
                                text="Título da tarefa",
                                font=("Arial", 12),
                                bg="#f0f0f0")

        rotuloTitulo.grid(row=0,
                          column=0,
                          sticky='e',
                          padx=5,
                          pady=5)

        self.entradaTitulo = tk.Entry(quadroEntrada,
                                      width=55,
                                      font=("Arial", 11))

        self.entradaTitulo.grid(row=0,
                                column=1,
                                columnspan=3,
                                sticky='w',
                                padx=5,
                                pady=5)

        rotuloDescricao = tk.Label(quadroEntrada,
                                   text="Descrição da tarefa",
                                   font=("Arial", 12),
                                   bg="#f0f0f0")

        rotuloDescricao.grid(row=1,
                             column=0,
                             sticky='ne',
                             padx=5,
                             pady=5)

        self.textoDescricao = tk.Entry(quadroEntrada,
                                       width=55,
                                       font=("Arial", 12),
                                       )

        self.textoDescricao.grid(row=1,
                                 column=1,
                                 columnspan=3,
                                 sticky='w',
                                 padx=5,
                                 pady=5)


        rotuloStatus = tk.Label(quadroEntrada,
                                text="Idade",
                                font=("Arial", 12),
                                bg="#f0f0f0")

        rotuloStatus.grid(row=3,
                          column=0,
                          sticky='e',
                          padx=5,
                          pady=5)

        self.varStatus = tk.StringVar()

        self.comboStatus = ttk.Combobox(quadroEntrada,

                                        textvariable=self.varStatus,

                                        values=["Pendente", "Concluída"],

                                        state='readonly',

                                        font=("Arial", 11))

        self.comboStatus.grid(row=3,
                              column=1,
                              padx=5,
                              pady=5)

        self.comboStatus.current(0)

        quadroBotoes = tk.Frame(self,
                                bg="#f0f0f0")

        quadroBotoes.pack(pady=10)

        botaoAdcionar = tk.Button(quadroBotoes,

                                  text="Adcionar",

                                  command=self.adcionar,

                                  bg="#a5d6a7",

                                  font=("Arial", 11, "bold"),

                                  width=18)

        botaoAdcionar.grid(row=0, column=0, padx=10, pady=5)

        botaoAtualizar = tk.Button(quadroBotoes,

                                   text="Atualizar/Editar",

                                   command=self.atualizar,

                                   bg="#fff59d",

                                   font=("Arial", 11, "bold"),

                                   width=18)

        botaoAtualizar.grid(row=0, column=1, padx=10, pady=5)

        botaoExcluir = tk.Button(quadroBotoes,

                                 text="Excluir",

                                 command=self.excluir,

                                 bg="#ef9a9a",

                                 font=("Arial", 11, "bold"),

                                 width=18)

        botaoExcluir.grid(row=0, column=2, padx=10, pady=5)

        quadroFiltro = tk.Frame(self,
                                bg="#f0f0f0")

        quadroFiltro.pack(pady=10)

        rotuloFiltro = tk.Label(quadroFiltro,

                                text="Filtrar por Status",

                                font=("Arial", 12),

                                bg="#f0f0f0")

        rotuloFiltro.grid(row=0, column=0, padx=5)

        self.varFiltro = tk.StringVar()

        self.comboFiltro = ttk.Combobox(quadroFiltro,

                                        textvariable=self.varFiltro,

                                        values=["Todos", "Pendente", "Concluída"],

                                        state='readonly',

                                        font=("Arial", 11))

        self.comboFiltro.grid(row=0, column=1, padx=5)

        botaoFiltro = tk.Button(quadroFiltro,

                                text="Aplicar Filtro",

                                command=self.aplicarFiltro,

                                bg="#81d4fa",

                                font=("Arial", 11, "bold"),

                                width=15)

        botaoFiltro.grid(row=0,
                         column=2,
                         padx=5)

        quadroArvore = tk.Frame(self,
                                bg="#f0f0f0")

        quadroArvore.pack(padx=20,

                          fill='both',

                          expand=True)

        barraRolagem = tk.Scrollbar(quadroArvore,

                                    orient='vertical')

        barraRolagem.pack(side=tk.RIGHT,

                          fill=tk.Y)

        self.arvoreCadastro = ttk.Treeview(quadroArvore,
                                           columns=("Título da tarefa", "Descrição da tarefa", "Status"),
                                           show="headings",
                                           height=15,
                                           yscrollcommand=barraRolagem.set)

        self.arvoreCadastro.focus_set()

        self.arvoreCadastro.heading("Título da tarefa", text="Título da tarefa")

        self.arvoreCadastro.heading("Descrição da tarefa", text="Descrição da tarefa")

        self.arvoreCadastro.heading("Status", text="Status")

        self.arvoreCadastro.column("Título da tarefa", width=220)

        self.arvoreCadastro.column("Descrição da tarefa", width=480)

        self.arvoreCadastro.column("Status", width=120)

        self.arvoreCadastro.bind("<<TreeviewSelect>>", self.aoClicarCadastro)

        self.arvoreCadastro.pack(pady=10,
                                 padx=10,
                                 fill='both',
                                 expand=True)

        barraRolagem.configure(command=self.arvoreCadastro.yview)

        self.carregarCadastros()

        self.pack(fill="both", expand=True)

        self.grid(row=0, column=0, sticky="nsew")

    def adcionar(self):

        nome = self.entradaTitulo.get().strip()

        email = self.textoDescricao.get().strip()


        idade = self.varStatus.get()

        if not nome:
            messagebox.showwarning("Aviso", "O nome não pode estar vazio. ")
            return

        novoCadastro = {
            "Título da tarefa": nome,
            "Descrição da tarefa": email,
            "Status": idade
        }

        self.colecao.insert_one(novoCadastro)

        self.carregarCadastros()

        self.limparCamposEntrada()

        messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")

    def limparCamposEntrada(self):

        self.entradaTitulo.delete(0, tk.END)

        self.textoDescricao.delete(0, tk.END)


        self.varStatus.set("Pendente")

    def carregarCadastros(self, filtroIdade=None):
        self.arvoreCadastro.delete(*self.arvoreCadastro.get_children())

        consulta = {"Status": filtroIdade} if filtroIdade else {}
        cadastros = self.colecao.find(consulta)

        for cadastro in cadastros:
            self.arvoreCadastro.insert("", tk.END, values=(
                cadastro["Título da tarefa"], cadastro["Descrição da tarefa"], cadastro["Status"]),
                                       text=str(cadastro["_id"]))

    def atualizar(self):
        if not self.idCadastroSelecionado:
            messagebox.showwarning("Aviso", "Nenhum cadastro selecionado para atualizar.")
            return

        nome = self.entradaTitulo.get().strip()
        email = self.textoDescricao.get().strip()
        idade = self.varStatus.get().strip()

        if not nome:
            messagebox.showwarning("Aviso", "O nome do cadastro não pode estar vazio.")
            return

        dadosAtualizacao = {
            "$set": {
                "Título da tarefa": nome,
                "Descrição da tarefa": email,  #
                "Status": idade
            }
        }

        try:
            self.colecao.update_one({"_id": ObjectId(self.idCadastroSelecionado)}, dadosAtualizacao)
            self.carregarCadastros()
            self.limparCamposEntrada()
            self.idCadastroSelecionado = None
            messagebox.showinfo("Sucesso", "Cadastro atualizado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar cadastro: {e}")

    def aoClicarCadastro(self, event):
        selecionado = self.arvoreCadastro.selection()
        if not selecionado:
            self.idCadastroSelecionado = None
            return

        self.idCadastroSelecionado = self.arvoreCadastro.item(selecionado[0], "text")

        try:
            dadosCadastro = self.colecao.find_one({"_id": ObjectId(self.idCadastroSelecionado)})
            if dadosCadastro:
                self.entradaTitulo.insert(tk.END, dadosCadastro["Título da tarefa"])
                self.textoDescricao.insert(tk.END, dadosCadastro["Descrição da tarefa"])
                self.varStatus.set(dadosCadastro["Status"])

            else:
                self.idCadastroSelecionado = None
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao buscar cadastro: {e}")
            self.idCadastroSelecionado = None

    def excluir(self):
        if not hasattr(self, 'idCadastroSelecionado') or not self.idCadastroSelecionado:
            messagebox.showwarning("Aviso", "Nenhum cadastro selecionado para excluir.")
            return

        resposta = messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir este cadastro?")
        if not resposta:
            return

        try:
            if not isinstance(self.idCadastroSelecionado, ObjectId):
                self.idCadastroSelecionado = ObjectId(self.idCadastroSelecionado)

            resultado = self.colecao.delete_one({"_id": self.idCadastroSelecionado})

            if resultado.deleted_count > 0:
                messagebox.showinfo("Sucesso", "Cadastro excluído com sucesso!")
            else:
                messagebox.showwarning("Aviso", "Nenhum cadastro foi excluído. Verifique o ID.")

            self.carregarCadastros()
            self.idCadastroSelecionado = None
            self.limparCamposEntrada()

        except Exception as e:
            print(f"Erro ao excluir cadastro: {e}")
            messagebox.showerror("Erro", f"Erro ao excluir cadastro: {e}")

    def aplicarFiltro(self):

        filtroEscolhido = self.varFiltro.get()

        if filtroEscolhido == "Todos":
            self.carregarCadastros()

        else:
            self.carregarCadastros(filtroIdade=filtroEscolhido)

janela = tk.Tk()
app = TarefaApp(janela)
janela.mainloop()


