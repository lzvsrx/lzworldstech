import sqlite3
from datetime import datetime
import pandas as pd

def init_db():
    conn = sqlite3.connect('lz_database.db', check_same_thread=False)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS contatos 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  nome TEXT, email TEXT, mensagem TEXT, data TEXT)''')
    conn.commit()
    conn.close()

def salvar_contato(nome, email, msg):
    conn = sqlite3.connect('lz_database.db', check_same_thread=False)
    c = conn.cursor()
    data_envio = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    c.execute("INSERT INTO contatos (nome, email, mensagem, data) VALUES (?, ?, ?, ?)", 
              (nome, email, msg, data_envio))
    conn.commit()
    conn.close()

def listar_mensagens():
    conn = sqlite3.connect('lz_database.db', check_same_thread=False)
    df = pd.read_sql_query("SELECT * FROM contatos ORDER BY id DESC", conn)
    conn.close()
    return df