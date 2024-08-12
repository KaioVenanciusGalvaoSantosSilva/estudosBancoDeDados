"""CREATE TABLE pessoa (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    idade INT
);
"""

import mysql.connector
from mysql.connector import Error
from tkinter import *



# Função para inserir dados no banco de dados
def inserir_dados():
    nome = entrada_nome.get()
    email = entrada_email.get()
    idade = entrada_idade.get()
    
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
            # Comando SQL para inserir dados na tabela
            query = "INSERT INTO pessoa (nome, email, idade) VALUES (%s, %s, %s)"
            values = (nome, email, idade)
            cursor.execute(query, values)
            conn.commit()
            resultado["text"] = "Dados inseridos com sucesso!"
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
app.title("Inserir Dados no Banco de Dados")
app.geometry("400x300")

# Rótulos e entradas de texto
rotulo_nome = Label(app, text="Nome:")
rotulo_nome.pack(pady=5)
entrada_nome = Entry(app)
entrada_nome.pack(pady=5)

rotulo_email = Label(app, text="Email:")
rotulo_email.pack(pady=5)
entrada_email = Entry(app)
entrada_email.pack(pady=5)

rotulo_idade = Label(app, text="Idade:")
rotulo_idade.pack(pady=5)
entrada_idade = Entry(app)
entrada_idade.pack(pady=5)

# Botão para inserir os dados
botao_inserir = Button(app, text="Inserir Dados", command=inserir_dados)
botao_inserir.pack(pady=20)

# Rótulo para exibir o resultado
resultado = Label(app, text="")
resultado.pack(pady=10)

# Inicia a interface gráfica
app.mainloop()
