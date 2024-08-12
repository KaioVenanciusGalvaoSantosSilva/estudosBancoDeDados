import mysql.connector
from mysql.connector import Error
from tkinter import *
from tkinter import ttk

#Codificação Dinâmica

# Função para obter os dados da tabela e os nomes das colunas
def obter_dados_e_colunas():
    try:
        # Conectando ao servidor MySQL (substitua user, password e database conforme necessário)
        conn = mysql.connector.connect(
            host='localhost',
            user='root',  # Substitua pelo seu usuário do MySQL
            password='',  # Substitua pela sua senha do MySQL
            database='nomebd'  # Substitua pelo nome do seu banco de dados
        )
        
        if conn.is_connected():
            nome_tabela = 'pessoa'
            cursor = conn.cursor()
            # Substitua 'pessoa' pelo nome da sua tabela
            cursor.execute(f"SELECT * FROM {nome_tabela}")
            
            # Obtém os dados da tabela
            rows = cursor.fetchall()
            
            # Obtém os nomes das colunas
            column_names = [desc[0] for desc in cursor.description]
            
            return column_names, rows
        else:
            return [], []
        
    except Error as e:
        print(f"Erro: {e}")
        return [], []
    
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Função para atualizar a exibição dos dados
def atualizar_tabela():
    for row in tree.get_children():
        tree.delete(row)
    
    colunas, dados = obter_dados_e_colunas()
    
    # Configura as colunas dinamicamente
    tree["columns"] = colunas
    for col in colunas:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor='center')
    
    # Insere os dados na tabela
    for row in dados:
        tree.insert("", END, values=row)

# Configurando a interface gráfica
app = Tk()
app.title("Visualizar Dados do Banco de Dados")
app.geometry("800x600")

# Configuração da tabela (Treeview)
tree = ttk.Treeview(app, show='headings')
tree.pack(expand=True, fill=BOTH, padx=10, pady=10)

# Botão para atualizar a tabela
botao_atualizar = Button(app, text="Atualizar", command=atualizar_tabela)
botao_atualizar.pack(pady=10)

# Inicia a interface gráfica
atualizar_tabela()  # Atualiza a tabela ao iniciar o aplicativo
app.mainloop()
