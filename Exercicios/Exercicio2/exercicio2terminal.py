import mysql.connector
from mysql.connector import Error

# Função para criar a tabela no banco de dados
def criar_tabela(nome_tabela):
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
            # Comando SQL para criar a tabela com os campos id, nome, telefone e email
            cursor.execute(f"""
                CREATE TABLE {nome_tabela} (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(255) NOT NULL,
                    telefone VARCHAR(20),
                    email VARCHAR(255)
                )
            """)
            print(f"Tabela '{nome_tabela}' criada com sucesso!")
        else:
            print("Erro ao conectar ao MySQL.")
        
    except Error as e:
        print(f"Erro: {e}")
    
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Função principal para capturar a entrada do usuário e criar a tabela
def main():
    nome_tabela = input("Digite o nome da tabela que deseja criar: ")  # Solicita o nome da tabela ao usuário
    criar_tabela(nome_tabela)  # Chama a função para criar a tabela

# Executa a função principal
if __name__ == "__main__":
    main()
