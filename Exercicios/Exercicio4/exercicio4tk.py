import mysql.connector
from mysql.connector import Error
from tkinter import *
from tkinter import ttk

# Função para obter dados da tabela
def obter_dados():
    try:
        # Conectando ao servidor MySQL (substitua user, password e database conforme necessário)
        conn = mysql.connector.connect(
            host='localhost',
            user='root',  # Substitua pelo seu usuário do MySQL
            password='',  # Substitua pela sua senha do MySQL
            database='kaio6'  # Substitua pelo nome do seu banco de dados
        )
        
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM pessoa")  # Substitua "pessoa" pelo nome da sua tabela
            rows = cursor.fetchall()
            return rows
        else:
            return []
        
    except Error as e:
        print(f"Erro: {e}")
        return []
    
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Função para atualizar a exibição dos dados
def atualizar_tabela():
    for row in tree.get_children():
        tree.delete(row)
    
    dados = obter_dados()
    for row in dados:
        tree.insert("", END, values=row)

# Configurando a interface gráfica
app = Tk()
app.title("Visualizar Dados do Banco de Dados")
app.geometry("600x400")

# Configuração da tabela (Treeview)
colunas = ("id", "nome", "email", "idade")  # Colunas da tabela
tree = ttk.Treeview(app, columns=colunas, show='headings')
tree.heading("id", text="ID")
tree.heading("nome", text="Nome")
tree.heading("email", text="Email")
tree.heading("idade", text="Idade")

tree.pack(expand=True, fill=BOTH, padx=10, pady=10)

# Botão para atualizar a tabela
botao_atualizar = Button(app, text="Atualizar", command=atualizar_tabela)
botao_atualizar.pack(pady=10)

# Inicia a interface gráfica
atualizar_tabela()  # Atualiza a tabela ao iniciar o aplicativo
app.mainloop()
