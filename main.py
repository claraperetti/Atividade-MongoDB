import tkinter as tk

from pymongo import  MongoClient

from ctypes import windll

from tkinter import ttk, messagebox

from bson.objectid import ObjectId

from bson import ObjectId

class SistemaCadastroApp:

    def __init__ (self, janela):


        self.janela = janela

        self.janela.title("Sistema de cadastro")

        self.janela.geometry("950x700")

        self.janela.configure(bg = "#f0f0f0")

        self.cliente = MongoClient("mongodb://localhost:27017")

        self.bd = self.cliente["cadastroUsuarios"]

        self.colecao = self.bd["Cadastro"]

        estilo = ttk.Style()

        estilo.theme_use('default')

        estilo.configure("Treeview",
                         background = "#ffffff",
                         foreground = "black",
                         rowheight = 25,
                         fielbackground = "#ffffff",
                         font = ("Arial", 11))

        estilo.configure("Treeview.Heading",
                         font = ("Arial", 12, "bold"))

        estilo.map("Treeview",

                   background = [("selected", "black")],
                   foreground = [("selected", "white")])

        quadroEntrada = tk.Frame(self.janela,
                                 bg="#f0f0f0")

        quadroEntrada.pack(pady=10,
                           padx=10,
                           fill="x")

        rotuloTitulo = tk.Label(quadroEntrada,
                                text="Nome",
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
                          columnspan= 3,
                          sticky='w',
                          padx=5,
                          pady=5)

        rotuloDescricao = tk.Label(quadroEntrada,
                                   text="E-mail",
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


        rotuloTelefone = tk.Label(quadroEntrada,
                                   text="Telefone",
                                   font=("Arial", 12),
                                   bg="#f0f0f0")

        rotuloTelefone.grid(row=2,
                             column=0,
                             sticky='ne',
                             padx=5,
                             pady=5)

        self.textoTelefone = tk.Entry(quadroEntrada,
                                       width=55,
                                       font=("Arial", 12),
                                       )

        self.textoTelefone.grid(row=2,
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

                                        textvariable= self.varStatus,

                                        values= ["Menor de idade", "Maior de idade"],

                                        state='readonly',

                                        font=("Arial", 11))

        self.comboStatus.grid(row=3,
                          column=1,
                          padx=5,
                          pady=5)

        self.comboStatus.current(0)

        quadroBotoes = tk.Frame(self.janela,
                                bg = "#f0f0f0")

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

        quadroFiltro = tk.Frame(self.janela,
                                bg="#f0f0f0")

        quadroFiltro.pack (pady=10)

        rotuloFiltro = tk.Label(quadroFiltro,

                                text="Filtrar por Idade",

                                font=("Arial", 12),

                                bg="#f0f0f0")

        rotuloFiltro.grid(row=0, column=0, padx=5)

        self.varFiltro = tk.StringVar()

        self.comboFiltro = ttk.Combobox(quadroFiltro,

                                        textvariable=self.varFiltro,

                                        values=["Todos", "Menor de idade", "Maior de idade"],

                                        state= 'readonly',

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

        quadroArvore = tk.Frame(self.janela,
                                 bg="#f0f0f0")

        quadroArvore.pack(padx=20,

                          fill='both',

                          expand=True)

        barraRolagem = tk.Scrollbar(quadroArvore,

                                    orient='vertical')

        barraRolagem.pack(side=tk.RIGHT,

                          fill=tk.Y)

        self.arvoreCadastro = ttk.Treeview(quadroArvore,
                                           columns=("Nome", "E-mail", "Telefone", "Idade"),

                                           show= "headings",
                                           height=15,
                                           yscrollcommand=barraRolagem.set)

        self.arvoreCadastro.focus_set()

        self.arvoreCadastro.heading("Nome", text="Nome")

        self.arvoreCadastro.heading("E-mail", text="E-mail")

        self.arvoreCadastro.heading("Telefone", text="Telefone")

        self.arvoreCadastro.heading("Idade", text="Idade")

        self.arvoreCadastro.column("Nome", width=220)

        self.arvoreCadastro.column("E-mail", width=480)

        self.arvoreCadastro.column("Telefone", width=220)

        self.arvoreCadastro.column("Idade",  width=120)

        self.arvoreCadastro.bind("<<TreeviewSelect>>", self.aoClicarCadastro)
        print("Bind de clique configurado!")  # Verifica se o bind foi chamado

        self.arvoreCadastro.pack(pady=10,
                                 padx=10,
                                 fill='both',
                                 expand=True)

        barraRolagem.configure(command=self.arvoreCadastro.yview)

        #self.arvoreCadastro =  None

        self.carregarCadastros()

        self.telaCadastro = tk.Frame(janela)
        self.telaTarefa = tk.Frame(janela)

        # Frame do menu superior
        menu_superior = tk.Frame(janela, bg="#f0c808")  # Cor amarelinha combinando com abelhas 🐝
        menu_superior.pack(fill=tk.X)

        # Botão para ir para a tela de cadastro
        btn_cadastro = tk.Button(menu_superior, text="Cadastro de Pessoas",
                                 bg="#fff", fg="#000", font=("Arial", 10, "bold"),
                                 command=lambda: self.alternar_tela("cadastro"))
        btn_cadastro.pack(side=tk.LEFT, padx=10, pady=10)

        # Botão para ir para a tela de tarefas
        btn_tarefas = tk.Button(menu_superior, text="Cadastro de Tarefas",
                                bg="#fff", fg="#000", font=("Arial", 10, "bold"),
                                command=lambda: self.alternar_tela("tarefas"))
        btn_tarefas.pack(side=tk.LEFT, padx=10, pady=10)

        self.alternar_tela("cadastro")

    def alternar_tela(self, tela):
        # Esconde ambas as telas
        self.telaCadastro.pack_forget()
        self.telaTarefa.pack_forget()

        # Exibe a tela solicitada
        if tela == "cadastro":
            self.telaCadastro.pack(fill="both", expand=True)
        elif tela == "tarefas":
            self.telaTarefa.pack(fill="both", expand=True)

    def abrir_tela_tarefas(self):
        TarefaApp(tk.Toplevel(self.janela), self.banco)

    def adcionar(self):

        nome = self.entradaTitulo.get().strip()

        email = self.textoDescricao.get().strip()

        telefone = self.textoTelefone.get().strip()

        idade = self.varStatus.get()

        if not nome:
            messagebox.showwarning("Aviso", "O nome não pode estar vazio. ")
            return

        novoCadastro = {
            "Nome" : nome,
            "E-mail" : email,
            "Telefone": telefone,
            "Idade" : idade
        }

        self.colecao.insert_one(novoCadastro)

        self.carregarCadastros()

        self.limparCamposEntrada()

        messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")

    def limparCamposEntrada(self):

        self.entradaTitulo.delete(0, tk.END)

        self.textoDescricao.delete(0, tk.END)

        self.textoTelefone.delete(0, tk.END)

        self.varStatus.set("Menor de idade")

    def carregarCadastros(self, filtroIdade=None):
        self.arvoreCadastro.delete(*self.arvoreCadastro.get_children())

        consulta = {"Idade": filtroIdade} if filtroIdade else {}
        cadastros = self.colecao.find(consulta)

        for cadastro in cadastros:
            self.arvoreCadastro.insert("", tk.END, values=(
            cadastro["Nome"], cadastro["E-mail"], cadastro["Telefone"], cadastro["Idade"]),
                                       text=str(cadastro["_id"]))  # Agora o ID está no 'text'

    def atualizar(self):
        if not self.idCadastroSelecionado:
            messagebox.showwarning("Aviso", "Nenhum cadastro selecionado para atualizar.")
            return

        nome = self.entradaTitulo.get().strip()
        email = self.textoDescricao.get().strip()
        telefone = self.textoTelefone.get().strip()
        idade = self.varStatus.get().strip()

        if not nome:
            messagebox.showwarning("Aviso", "O nome do cadastro não pode estar vazio.")
            return

        dadosAtualizacao = {
            "$set": {
                "Nome": nome,
                "E-mail": email,  # Corrigido para ser igual ao que foi salvo
                "Telefone": telefone,
                "Idade": idade
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

        self.idCadastroSelecionado = self.arvoreCadastro.item(selecionado[0], "text")  # Pegando o ID do 'text'

        try:
            dadosCadastro = self.colecao.find_one({"_id": ObjectId(self.idCadastroSelecionado)})
            if dadosCadastro:
                self.entradaTitulo.delete(0, tk.END)
                self.entradaTitulo.insert(tk.END, dadosCadastro["Nome"])

                self.textoDescricao.delete(0, tk.END)
                self.textoDescricao.insert(tk.END, dadosCadastro["E-mail"])

                self.textoTelefone.delete(0, tk.END)
                self.textoTelefone.insert(tk.END, dadosCadastro["Telefone"])

                self.varStatus.set(dadosCadastro["Idade"])
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
            return  # Se o usuário cancelar, nada acontece

        try:
            # Converte para ObjectId se ainda não estiver no formato correto
            if not isinstance(self.idCadastroSelecionado, ObjectId):
                self.idCadastroSelecionado = ObjectId(self.idCadastroSelecionado)

            # Exclui do MongoDB
            resultado = self.colecao.delete_one({"_id": self.idCadastroSelecionado})

            if resultado.deleted_count > 0:
                messagebox.showinfo("Sucesso", "Cadastro excluído com sucesso!")
            else:
                messagebox.showwarning("Aviso", "Nenhum cadastro foi excluído. Verifique o ID.")

            # Atualiza a Treeview
            self.carregarCadastros()
            self.idCadastroSelecionado = None  # Reseta a seleção
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



    def formatar_telefone(self, event):
        texto = self.textoTelefone.get().replace("(", "").replace(")", "").replace("-", "").replace(" ", "")

        if len(texto) > 11:
            texto = texto[:11]

        formatado = ""
        if len(texto) >= 2:
            formatado += f"({texto[:2]}) "
        if len(texto) >= 7:
            formatado += f"{texto[2:7]}-{texto[7:]}"
        else:
            formatado += texto[2:]

        self.textoTelefone.unbind("<KeyRelease>")

        self.textoTelefone.delete(0, tk.END)
        self.textoTelefone.insert(0, formatado)

        self.textoTelefone.bind("<KeyRelease>", self.formatar_telefone)

class TarefaApp(tk.Frame):
    def __init__(self, master, db):
        super().__init__(master, bg="#f7f7f7")
        self.master = master
        self.db = db
        self.colecao = db["tarefas"]
        self.idTarefaSelecionada = None

        self.criar_widgets()
        self.carregar_tarefas()

    def criar_widgets(self):
        # Título
        lblTitulo = tk.Label(self, text="Cadastro de Tarefas", font=("Arial", 18, "bold"), bg="#f7f7f7")
        lblTitulo.pack(pady=10)

        # Container dos campos
        frameCampos = tk.Frame(self, bg="#f7f7f7")
        frameCampos.pack(pady=10)

        # Título da tarefa
        tk.Label(frameCampos, text="Título:", bg="#f7f7f7").grid(row=0, column=0, sticky="e")
        self.entradaTitulo = tk.Entry(frameCampos, width=40)
        self.entradaTitulo.grid(row=0, column=1, padx=5, pady=5)

        # Descrição
        tk.Label(frameCampos, text="Descrição:", bg="#f7f7f7").grid(row=1, column=0, sticky="e")
        self.entradaDescricao = tk.Entry(frameCampos, width=40)
        self.entradaDescricao.grid(row=1, column=1, padx=5, pady=5)

        # Status
        tk.Label(frameCampos, text="Status:", bg="#f7f7f7").grid(row=2, column=0, sticky="e")
        self.statusVar = tk.StringVar()
        self.comboStatus = ttk.Combobox(frameCampos, textvariable=self.statusVar, values=["Pendente", "Completa"], state="readonly", width=37)
        self.comboStatus.grid(row=2, column=1, padx=5, pady=5)
        self.comboStatus.set("Pendente")

        # Botões
        frameBotoes = tk.Frame(self, bg="#f7f7f7")
        frameBotoes.pack(pady=10)

        btnAdicionar = tk.Button(frameBotoes, text="Adicionar", command=self.adicionar_tarefa, bg="#4caf50", fg="white", width=12)
        btnAdicionar.grid(row=0, column=0, padx=5)

        btnAtualizar = tk.Button(frameBotoes, text="Atualizar", command=self.atualizar_tarefa, bg="#2196f3", fg="white", width=12)
        btnAtualizar.grid(row=0, column=1, padx=5)

        btnExcluir = tk.Button(frameBotoes, text="Excluir", command=self.excluir_tarefa, bg="#f44336", fg="white", width=12)
        btnExcluir.grid(row=0, column=2, padx=5)

        # Treeview
        colunas = ("Título", "Descrição", "Status")
        self.arvoreTarefas = ttk.Treeview(self, columns=colunas, show="headings", height=10)
        for col in colunas:
            self.arvoreTarefas.heading(col, text=col)
            self.arvoreTarefas.column(col, width=150)

        self.arvoreTarefas.pack(pady=10)
        self.arvoreTarefas.bind("<<TreeviewSelect>>", self.selecionar_tarefa)

    def adicionar_tarefa(self):
        titulo = self.entradaTitulo.get().strip()
        descricao = self.entradaDescricao.get().strip()
        status = self.statusVar.get()

        if not titulo:
            messagebox.showwarning("Aviso", "O título não pode estar vazio.")
            return

        novaTarefa = {
            "Título": titulo,
            "Descrição": descricao,
            "Status": status
        }

        self.colecao.insert_one(novaTarefa)
        self.limpar_campos()
        self.carregar_tarefas()
        messagebox.showinfo("Sucesso", "Tarefa adicionada com sucesso!")

    def atualizar_tarefa(self):
        if not self.idTarefaSelecionada:
            messagebox.showwarning("Aviso", "Selecione uma tarefa para atualizar.")
            return

        try:
            titulo = self.entradaTitulo.get().strip()
            descricao = self.entradaDescricao.get().strip()
            status = self.statusVar.get()

            self.colecao.update_one(
                {"_id": ObjectId(self.idTarefaSelecionada)},
                {"$set": {"Título": titulo, "Descrição": descricao, "Status": status}}
            )
            self.limpar_campos()
            self.carregar_tarefas()
            messagebox.showinfo("Sucesso", "Tarefa atualizada com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def excluir_tarefa(self):
        if not self.idTarefaSelecionada:
            messagebox.showwarning("Aviso", "Selecione uma tarefa para excluir.")
            return

        self.colecao.delete_one({"_id": ObjectId(self.idTarefaSelecionada)})
        self.limpar_campos()
        self.carregar_tarefas()
        messagebox.showinfo("Sucesso", "Tarefa excluída com sucesso!")

    def carregar_tarefas(self):
        for item in self.arvoreTarefas.get_children():
            self.arvoreTarefas.delete(item)

        for tarefa in self.colecao.find():
            self.arvoreTarefas.insert("", "end", iid=str(tarefa["_id"]), values=(tarefa["Título"], tarefa["Descrição"], tarefa["Status"]))

    def selecionar_tarefa(self, event):
        selecionado = self.arvoreTarefas.selection()
        if selecionado:
            self.idTarefaSelecionada = selecionado[0]
            dados = self.colecao.find_one({"_id": ObjectId(self.idTarefaSelecionada)})
            if dados:
                self.entradaTitulo.delete(0, tk.END)
                self.entradaTitulo.insert(0, dados["Título"])
                self.entradaDescricao.delete(0, tk.END)
                self.entradaDescricao.insert(0, dados["Descrição"])
                self.statusVar.set(dados["Status"])

    def limpar_campos(self):
        self.entradaTitulo.delete(0, tk.END)
        self.entradaDescricao.delete(0, tk.END)
        self.statusVar.set("Pendente")
        self.idTarefaSelecionada = None

janelaPrincipal = tk.Tk()

app = SistemaCadastroApp(janelaPrincipal)

janelaPrincipal.mainloop()


