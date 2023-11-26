from tkinter import *
from tkinter import ttk
import mysql.connector

root = Tk()

class Funcs():
    def limpa_tela(self):
        self.id_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.valor_entry.delete(0, END)
        self.desc_entry.delete(0, END)

    def conecta_bd(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="bruno2255",
            database="bd_loja"
        )
        self.cursor = self.conexao.cursor()
        print("Conectando ao banco de dados")

    def desconecta_bd(self):
        self.cursor.close()
        print("Desconectando ao banco de dados")
        self.conexao.close()

    def criar_tabela(self):
        self.conecta_bd()

        # Criação da tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS vendas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                produto VARCHAR(255) NOT NULL,
                preco DECIMAL(10, 2) NOT NULL,
                descricao VARCHAR(255) NULL DEFAULT NULL
            )
        """)
        print("Banco de dados criado")
        self.conexao.commit()
        self.desconecta_bd()
    def variaveis(self):
        self.ID = self.id_entry.get()
        self.nome = self.nome_entry.get()
        self.valor = self.valor_entry.get()
        self.desc = self.desc_entry.get()
    def add_produto(self):
        self.variaveis()
        self.conecta_bd()

        self.cursor.execute("INSERT INTO vendas (produto, preco, descricao) VALUES (%s, %s, %s)",
                            (self.nome, self.valor, self.desc))
        self.conexao.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()

    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()
        self.cursor.execute("SELECT id, produto, preco, descricao FROM vendas ORDER BY id ASC;")
        lista = self.cursor.fetchall()

        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.desconecta_bd()

    def OnDoubleClick(self, event):
        self.limpa_tela()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1, col2, col3, col4 = self.listaCli.item(n, "values")
            self.id_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.valor_entry.insert(END, col3)
            self.desc_entry.insert(END, col4)
            
    def delete_produto(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(f"""DELETE FROM vendas WHERE id = {self.ID} """)
        self.conexao.commit()
        self.desconecta_bd()
        self.limpa_tela()
        self.select_lista()
    def alterar_produto(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute("UPDATE vendas SET produto = %s, preco = %s, descricao = %s WHERE id = %s",
                        (self.nome, self.valor, self.desc, self.ID))
        self.conexao.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()
    def buscar_produto(self):
        self.conecta_bd()
        self.listaCli.delete(*self.listaCli.get_children())
        
        self.nome_entry.insert(END, '%')
        nome = self.nome_entry.get()
        self.cursor.execute(
    """SELECT id, produto, preco, descricao FROM vendas WHERE produto LIKE %s ORDER BY produto ASC""",
    ('%' + nome + '%',)
)
        buscarnomeCli = self.cursor.fetchall()
        for i in buscarnomeCli:
            self.listaCli.insert("", END, values=i)
        self.limpa_tela()

        self.desconecta_bd()

class app(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.criar_tabela()
        self.select_lista()
        root.mainloop()

    def tela(self):
        self.root.title("Gerenciador de Vendas")
        self.root.configure(background="#1e3743")
        self.root.geometry("700x500")  # tamanho da tela
        self.root.resizable(True, True)  # tela responsiva, sim ou não
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=700, height=500)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets_frame1(self):
        # criar botão limpar
        self.bt_limpar = Button(self.frame_1, text="Limpar", bd=2, bg="#107db2", fg="white",
                                font=('verdana', 8, 'bold'), command=self.limpa_tela)

        self.bt_limpar.place(relx=0.2, rely=0.2, relwidth=0.1, relheight=0.15)
        # botao buscar
        self.bt_buscar = Button(self.frame_1, text="Buscar", bd=2, bg="#107db2", fg="white",
                                font=('verdana', 8, 'bold'), command= self.buscar_produto)
        self.bt_buscar.place(relx=0.3, rely=0.2, relwidth=0.1, relheight=0.15)
        # botao novo
        self.bt_novo = Button(self.frame_1, text="Novo", bd=2, bg="#107db2", fg="white",
                              font=('verdana', 8, 'bold'), command=self.add_produto)
        self.bt_novo.place(relx=0.6, rely=0.2, relwidth=0.1, relheight=0.15)
        # botao alterar
        self.bt_alterar = Button(self.frame_1, text="Alterar", bd=2, bg="#107db2", fg="white",
                                 font=('verdana', 8, 'bold'), command= self.alterar_produto)
        self.bt_alterar.place(relx=0.7, rely=0.2, relwidth=0.1, relheight=0.15)
        # botao apagar
        self.bt_apagar = Button(self.frame_1, text="Apagar", bd=2, bg="#107db2", fg="white",
                                font=('verdana', 8, 'bold'), command= self.delete_produto)
        self.bt_apagar.place(relx=0.8, rely=0.2, relwidth=0.1, relheight=0.15)

        # criação label e entrada do ID
        self.lbid = Label(self.frame_1, text="ID", bg='#dfe3ee', fg='#107db2')
        self.lbid.place(relx=0.05, rely=0.16)

        self.id_entry = Entry(self.frame_1)
        self.id_entry.place(relx=0.05, rely=0.25, relwidth=0.05)

        # criação nome Produto
        self.lbnome = Label(self.frame_1, text="Produto", bg='#dfe3ee', fg='#107db2')
        self.lbnome.place(relx=0.05, rely=0.40)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.50, relwidth=0.2)

        # criação botão valor
        self.lbvalor = Label(self.frame_1, text="Valor", bg='#dfe3ee', fg='#107db2')
        self.lbvalor.place(relx=0.5, rely=0.40)

        self.valor_entry = Entry(self.frame_1)
        self.valor_entry.place(relx=0.5, rely=0.50, relwidth=0.2)

        # criação botão descrição
        self.lbdesc = Label(self.frame_1, text="Descrição", bg='#dfe3ee', fg='#107db2')
        self.lbdesc.place(relx=0.05, rely=0.60)

        self.desc_entry = Entry(self.frame_1)
        self.desc_entry.place(relx=0.05, rely=0.70, relwidth=0.65)

    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height=3, columns=("col1", "col2", "col3", "col4"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="ID")
        self.listaCli.heading("#2", text="Produto")
        self.listaCli.heading("#3", text="Valor")
        self.listaCli.heading("#4", text="Descrição")

        self.listaCli.column("#0", width=22)
        self.listaCli.column("#1", width=22)
        self.listaCli.column("#2", width=160)
        self.listaCli.column("#3", width=150)
        self.listaCli.column("#4", width=200)

        self.listaCli.place(relx=0.01, rely=0.02, relwidth=0.95, relheight=0.90)

        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscrollcommand=self.scroolLista.set)
        self.scroolLista.configure(command=self.listaCli.yview)
        self.scroolLista.place(relx=0.96, rely=0.02, relwidth=0.04, relheight=0.90)
        self.listaCli.bind("<Double-1>", self.OnDoubleClick)

app()
