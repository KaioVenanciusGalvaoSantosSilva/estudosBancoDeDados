import mysql.connector
from mysql.connector import Error
import bcrypt
from tkinter import *
from tkinter import messagebox

# Função para adicionar usuário ao banco de dados
def adicionar_usuario(usuario, senha):
    senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
    
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',  # Substitua pelo seu usuário do MySQL
            password='',  # Substitua pela sua senha do MySQL
            database='kaio6'  # Substitua pelo nome do seu banco de dados
        )
        
        if conn.is_connected():
            cursor = conn.cursor()
            query = "INSERT INTO usuarios (usuario, senha) VALUES (%s, %s)"
            cursor.execute(query, (usuario, senha_hash))
            conn.commit()
            messagebox.showinfo("Sucesso", "Usuário adicionado com sucesso!")
        else:
            messagebox.showerror("Erro", "Erro ao conectar ao MySQL.")
    
    except Error as e:
        messagebox.showerror("Erro", f"Erro: {e}")
    
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Função chamada quando o botão de cadastro é clicado
def cadastrar_usuario():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    
    if usuario and senha:
        adicionar_usuario(usuario, senha)
    else:
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")

# Configuração da interface gráfica
app = Tk()
app.title("Cadastro de Usuário")
app.geometry("300x200")

# Rótulos e campos de entrada
rotulo_usuario = Label(app, text="Usuário:")
rotulo_usuario.pack(pady=5)
entrada_usuario = Entry(app)
entrada_usuario.pack(pady=5)

rotulo_senha = Label(app, text="Senha:")
rotulo_senha.pack(pady=5)
entrada_senha = Entry(app, show='*')  # 'show' oculta o texto da senha
entrada_senha.pack(pady=5)

# Botão para cadastrar o usuário
botao_cadastrar = Button(app, text="Cadastrar", command=cadastrar_usuario)
botao_cadastrar.pack(pady=20)

# Inicia a interface gráfica
app.mainloop()
