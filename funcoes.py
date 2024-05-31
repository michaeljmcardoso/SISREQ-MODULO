import sqlite3

def conectar_banco_de_dados():
  try:
    conn = sqlite3.connect('banco_dados.db')
    return conn
  except sqlite3.Error as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
    return None

def criar_tabela_se_nao_existir(conn):
  cursor = conn.cursor()
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
      id INTERGER PRIMARY KEY,
      nome TEXT,
      email TEXT,
      senha TEXT
    )
  """)
  conn.commit()

# incluir funções do programa
