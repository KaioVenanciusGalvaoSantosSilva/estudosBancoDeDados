import mysql.connector
from mysql.connector import Error

# Função para obter dados da tabela e os nomes das colunas
def obter_dados_e_colunas():
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
            # Substitua 'pessoa' pelo nome da sua tabela
            cursor.execute("SELECT * FROM pessoa")
            
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

# Função para exibir os dados no terminal
def exibir_dados():
    colunas, dados = obter_dados_e_colunas()
    
    if not colunas:
        print("Nenhum dado encontrado ou erro na conexão.")
        return
    
    # Imprime o cabeçalho das colunas
    print(" | ".join(colunas))
    print("-" * (len(" | ".join(colunas)) + 2))  # Linha de separação
    
    # Imprime os dados
    for row in dados:
        print(" | ".join(str(value) for value in row))

# Função principal para executar o script
def main():
    print("\n")
    exibir_dados()

# Executa a função principal
if __name__ == "__main__":
    main()
