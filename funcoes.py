import PySimpleGUI as sg
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
            id INTEGER PRIMARY KEY,
            nome TEXT,
            email TEXT,
            senha TEXT
        )
    """)
    conn.commit()

def inserir_dados(values, janela):
    nome = values['-NOME-']
    email = values['-EMAIL-']
    senha = values['-SENHA-']

    conn = conectar_banco_de_dados()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute(''' 
                       INSERT INTO usuarios (
                       'nome',
                       'email',
                       'senha') 
                       VALUES (?, ?, ?)
                       ''',
                       (
                         nome,
                         email,
                         senha
                       )
        )

        conn.commit()
        sg.popup('Dados inseridos com sucesso!', title='Sucesso')

        janela['-NOME-'].update('')
        janela['-EMAIL-'].update('')
        janela['-SENHA-'].update('') 

        cursor.close()
        conn.close()

def consultar_registros(janela):
    conn = conectar_banco_de_dados()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        registros = cursor.fetchall()
        if registros:
            janela['-TABLE-'].update(registros)
        else:
            sg.popup('Não há registros cadastrados.', title='Registros')

        cursor.close()
        conn.close()
