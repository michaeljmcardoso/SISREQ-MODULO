import PySimpleGUI as sg
import funcoes
import sqlite3

conn = sqlite3.connect('banco_dados.db')
cursor = conn.cursor()

sg.theme('Darkgreen')
layout = [
            [sg.Text('Nome:'), sg.Input(key='-NOME-', size=(20, 1))], 
            [sg.Text('Email:'), sg.Input(key='-EMAIL-', size=(20, 1))],
            [sg.Text('Senha:'), sg.Input(key='-SENHA-', size=(20, 1))],
            [sg.Button('INSERIR', button_color='#ac4e04'), sg.Button('CONSULTAR', button_color='green')],
            [sg.Table(
            values=[],
            headings=[
                'ID',
                'Nome',
                'Email',
                'Senha'
            ],
            num_rows=30,
            key='-TABLE-',
            hide_vertical_scroll=False,
            vertical_scroll_only=False,
            justification='left',
            auto_size_columns=False,
            )],
            [sg.Button('SAIR', button_color='#ac4e04')],]

janela = sg.Window("Sistema de Regularização Quilombola (v.0.01)", layout, resizable=True)

def inserir_dados(values):
  nome = values['-NOME-']
  email = values['-EMAIL-']
  senha = values['-SENHA-']

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

def consultarRegistros():
    cursor.execute("SELECT * FROM usuarios")
    registros = cursor.fetchall()
    if registros:
        janela['-TABLE-'].update(registros)
    else:
        sg.popup('Não há registros cadastrados.', title='Registros')

def main():
    conn = funcoes.conectar_banco_de_dados()
    if conn is not None:
        funcoes.criar_tabela_se_nao_existir(conn)

    while True:
        event, values = janela.read()
        if event == 'SAIR' or event == sg.WIN_CLOSED:
            break
        elif event == 'INSERIR':
            inserir_dados(values)
            consultarRegistros()
        elif event == 'CONSULTAR':
            consultarRegistros()

    janela.close()
    conn.close()

if __name__ == "__main__":
    main()
