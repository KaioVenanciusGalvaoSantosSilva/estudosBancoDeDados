"""CREATE TABLE pessoa (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    idade INT
);
"""

import mysql.connector
from mysql.connector import Error

# Função para inserir dados no banco de dados
def inserir_dados(nome, email, idade):
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
            print("Dados inseridos com sucesso!")
        else:
            print("Erro ao conectar ao MySQL.")
        
    except Error as e:
        print(f"Erro: {e}")
    
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Função principal para capturar a entrada do usuário e inserir os dados
def main():
    nome = input("Digite o nome: ")
    email = input("Digite o email: ")
    idade = input("Digite a idade: ")
    
    # Chama a função para inserir os dados
    inserir_dados(nome, email, idade)

# Executa a função principal
if __name__ == "__main__":
    main()
