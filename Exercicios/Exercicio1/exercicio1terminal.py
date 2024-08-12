"""Crie uma aplicação no python que solicite o nome do banco de dados que deseja criar e crie no SQL após o usuário digitar o nome e clicar em criar.

*Deve rodar o código abaixo antes de codificar (instalar o mysql)
pip install mysql-connector-python
"""
import mysql.connector
from mysql.connector import Error

# Função para criar o banco de dados
def criar_banco_de_dados(nome_banco):
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
            print(f"Banco de dados '{nome_banco}' criado com sucesso!")
        else:
            print("Erro ao conectar ao MySQL.")
        
    except Error as e:
        print(f"Erro: {e}")
    
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Função principal para capturar a entrada do usuário e criar o banco de dados
def main():
    nome_banco = input("Digite o nome do banco de dados que deseja criar: ")  # Solicita o nome do banco de dados
    criar_banco_de_dados(nome_banco)  # Chama a função para criar o banco de dados

# Executa a função principal
if __name__ == "__main__":
    main()
