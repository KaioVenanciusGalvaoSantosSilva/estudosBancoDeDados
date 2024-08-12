
"""CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL
);"""

import mysql.connector
from mysql.connector import Error
import bcrypt
from tkinter import *
from tkinter import messagebox

# Função para verificar as credenciais do usuário
def verificar_credenciais():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    
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
            query = "SELECT senha FROM usuarios WHERE usuario = %s"
            cursor.execute(query, (usuario,))
            resultado = cursor.fetchone()
            
            if resultado:
                senha_hash = resultado[0]
                if bcrypt.checkpw(senha.encode('utf-8'), senha_hash.encode('utf-8')):
                    mostrar_tela_conectado()
                else:
                    messagebox.showerror("Erro", "Usuário ou senha incorretos.")
            else:
                messagebox.showerror("Erro", "Usuário não encontrado.")
        
    except Error as e:
        messagebox.showerror("Erro", f"Erro: {e}")
    
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Função para mostrar a tela de "conectado"
def mostrar_tela_conectado():
    tela_login.pack_forget()  # Remove a tela de login
    tela_conectado.pack(pady=20)  # Mostra a tela de conectado

# Configurando a interface gráfica
app = Tk()
app.title("Login")
app.geometry("400x300")

# Tela de login
tela_login = Frame(app)
tela_login.pack(pady=20)

rotulo_usuario = Label(tela_login, text="Usuário:")
rotulo_usuario.pack(pady=5)
entrada_usuario = Entry(tela_login)
entrada_usuario.pack(pady=5)

rotulo_senha = Label(tela_login, text="Senha:")
rotulo_senha.pack(pady=5)
entrada_senha = Entry(tela_login, show='*')  # 'show' oculta o texto da senha
entrada_senha.pack(pady=5)

botao_login = Button(tela_login, text="Login", command=verificar_credenciais)
botao_login.pack(pady=20)

# Tela de conectado
tela_conectado = Frame(app)
rotulo_bem_vindo = Label(tela_conectado, text="Bem-vindo, você está conectado!")
rotulo_bem_vindo.pack(pady=20)

# Inicia a interface gráfica
app.mainloop()
