import mysql.connector
from mysql.connector import Error
import bcrypt

# Função para verificar as credenciais do usuário
def verificar_credenciais(usuario, senha):
    try:
        # Conectando ao servidor MySQL
        conn = mysql.connector.connect(
            host='localhost',
            user='root',  # Substitua pelo seu usuário do MySQL
            password='',  # Substitua pela sua senha do MySQL
            database='kaio6'  # Substitua pelo nome do seu banco de dados
        )
        
        if conn.is_connected():
            cursor = conn.cursor()
            query = "SELECT senha FROM usuarios WHERE usuario = %s"
            cursor.execute(query, (usuario,))
            resultado = cursor.fetchone()
            
            if resultado:
                senha_hash = resultado[0]
                if bcrypt.checkpw(senha.encode('utf-8'), senha_hash.encode('utf-8')):
                    print("Bem-vindo, você está conectado!")
                else:
                    print("Usuário ou senha incorretos.")
            else:
                print("Usuário não encontrado.")
        
    except Error as e:
        print(f"Erro: {e}")
    
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Solicitando entrada do usuário
usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

# Verificando as credenciais
verificar_credenciais(usuario, senha)
