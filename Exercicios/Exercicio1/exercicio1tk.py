"""Crie uma aplicação no python que solicite o nome do banco de dados que deseja criar e crie no SQL após o usuário digitar o nome e clicar em criar.

*Deve rodar o código abaixo antes de codificar (instalar o mysql)
pip install mysql-connector-python
"""

import mysql.connector
from mysql.connector import Error
from tkinter import *

# Função para criar o banco de dados
def criar_banco_de_dados():
    nome_banco = entrada_nome_banco.get()  # Obtém o nome do banco de dados a partir da entrada do usuário
    
    try:
        # Conectando ao servidor MySQL (substitua user e password conforme necessário)
        conn = mysql.connector.connect(
            host='localhost',
            user='root',  # Substitua pelo seu usuário do MySQL
            password=''  # Substitua pela sua senha do MySQL
        )
        
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(f"CREATE DATABASE {nome_banco}")
            resultado["text"] = f"Banco de dados '{nome_banco}' criado com sucesso!"
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
app.title("Criador de Banco de Dados MySQL")
app.geometry("600x200")

# Rótulo e entrada de texto
rotulo = Label(app, text="Nome do Banco de Dados:")
rotulo.pack(pady=10)

entrada_nome_banco = Entry(app)#campo para o usuário digitar
entrada_nome_banco.pack(pady=5)

# Botão para criar o banco de dados
botao_criar = Button(app, text="Criar", command=criar_banco_de_dados)
botao_criar.pack(pady=20)

# Rótulo para exibir o resultado
resultado = Label(app, text="")
resultado.pack(pady=10)

# Inicia a interface gráfica
app.mainloop()
