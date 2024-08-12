"""Crie uma aplicação no python que solicite o nome da tabela que deseja criar e crie no SQL após o usuário digitar o nome e clicar em criar."""

import mysql.connector
from mysql.connector import Error
from tkinter import *

# Função para criar a tabela no banco de dados
def criar_tabela():
    nome_tabela = entrada_nome_tabela.get()  # Obtém o nome da tabela a partir da entrada do usuário
    
    try:
        # Conectando ao servidor MySQL (substitua user e password conforme necessário)
        conn = mysql.connector.connect(
            host='localhost',
            user='root',  # Substitua pelo seu usuário do MySQL
            password='',  # Substitua pela sua senha do MySQL
            database='nomebd'  # Substitua pelo nome do seu banco de dados
        )
        
        if conn.is_connected():
            cursor = conn.cursor()
            # Comando SQL para criar uma tabela com uma coluna "id" como chave primária
            cursor.execute(f"CREATE TABLE {nome_tabela} (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255) NOT NULL, telefone VARCHAR(20), email VARCHAR(255))")
            resultado["text"] = f"Tabela '{nome_tabela}' criada com sucesso!"
        else:
            resultado["text"] = "Erro ao conectar ao MySQL."
        
    except Error as e:
        resultado["text"] = f"Erro: {e}"
    
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Configurando a interface gráfica
app = Tk()
app.title("Criador de Tabelas MySQL")
app.geometry("600x200")

# Rótulo e entrada de texto
rotulo = Label(app, text="Nome da Tabela:")
rotulo.pack(pady=10)

entrada_nome_tabela = Entry(app)  # Campo para o usuário digitar o nome da tabela
entrada_nome_tabela.pack(pady=5)

# Botão para criar a tabela
botao_criar = Button(app, text="Criar", command=criar_tabela)
botao_criar.pack(pady=20)

# Rótulo para exibir o resultado
resultado = Label(app, text="")
resultado.pack(pady=10)

# Inicia a interface gráfica
app.mainloop()
