import PySimpleGUI as sg
import relatorios
from funcoes_registro import conectar_banco_de_dados
from salvar import salvar_extrato_planilha
from constantes import FONTE, FONTE_DE_AVSIO, criar_tabela

"""Funções para a filtrar registros por fases do processo"""

def fase_inicial():
    conn = conectar_banco_de_dados()
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) as Total FROM SISREQ WHERE Fase_Processo LIKE '%Inicial%'")
    total_fase_inicial = cursor.fetchone()[0]

    cursor.execute("SELECT * FROM SISREQ WHERE Fase_Processo LIKE '%Inicial%'")
    registros = cursor.fetchall()

    if registros:
        layout = [
            [criar_tabela(registros)],
            [
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de processos: {total_fase_inicial} Aguardando Início dos Estudos de Identificação e Delimitação', font=FONTE_DE_AVSIO)
            ]
        ]

        janela = sg.Window('TERRITÓRIOS SEM ESTUDOS DE IDENTIFICAÇÃO E DELIMITAÇÃO.', layout, size=(1200, 700), resizable=True)

        while True:
            event, _ = janela.read()

            if event == sg.WINDOW_CLOSED or event == 'Fechar':
                break

            elif event == 'Extrato':
                salvar_extrato_planilha(registros)

        janela.close()

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=FONTE)


def fase_Rtid():
    conn = conectar_banco_de_dados()
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) as Total FROM SISREQ WHERE Fase_Processo LIKE '%Estudo de Identificação%'")
    total_fase_rtid = cursor.fetchone()[0]

    cursor.execute("SELECT * FROM SISREQ WHERE Fase_Processo LIKE '%Estudo de Identificação%'")
    registros = cursor.fetchall()

    if registros:
        layout = [
            [criar_tabela(registros)],
            [   
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de processos: {total_fase_rtid}', font=FONTE_DE_AVSIO), 
            ]
        ]

        janela = sg.Window('TERRITÓRIOS EM ESTUDO DE IDENTIFICAÇÃO E DELIMITAÇÃO', layout, size=(1200, 700), resizable=True)

        while True:
            event, _ = janela.read()

            if event == sg.WINDOW_CLOSED or event == 'Fechar':
                break

            elif event == 'Extrato':
                salvar_extrato_planilha(registros)

        janela.close()

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=FONTE)


def fase_publicacao():
    conn = conectar_banco_de_dados()
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) as Total FROM SISREQ WHERE Fase_Processo LIKE '%Publicação%'")
    total_fase_publicacao = cursor.fetchone()[0]

    cursor.execute("SELECT * FROM SISREQ WHERE Fase_Processo LIKE '%Publicação%'")
    registros = cursor.fetchall()

    if registros:
        layout = [
            [criar_tabela(registros)],
            [
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de processos: {total_fase_publicacao}', font=FONTE_DE_AVSIO)
            ]
        ]

        janela = sg.Window('PROCESSOS EM FASE DE PUBLICAÇÃO', layout, size=(1200, 700), resizable=True)

        while True:
            event, _ = janela.read()

            if event == sg.WINDOW_CLOSED or event == 'Fechar':
                break
            
            elif event == 'Extrato':
                salvar_extrato_planilha(registros)

        janela.close()

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=FONTE)
        

def fase_notificacao():
    conn = conectar_banco_de_dados()
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) as Total FROM SISREQ WHERE Fase_Processo LIKE '%Notificação%'")
    total_fase_notificacao = cursor.fetchone()[0]

    cursor.execute("SELECT * FROM SISREQ WHERE Fase_Processo LIKE '%Notificação%'")
    registros = cursor.fetchall()

    if registros:
        layout = [
            [criar_tabela(registros)],
            [
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de processos: {total_fase_notificacao}', font=FONTE_DE_AVSIO)
            ]
        ]

        janela = sg.Window('PROCESSOS EM FASE DE NOTIFICAÇÃO', layout, size=(1200, 700), resizable=True)

        while True:
            event, _ = janela.read()

            if event == sg.WINDOW_CLOSED or event == 'Fechar':
                break

            elif event == 'Extrato':
                salvar_extrato_planilha(registros)

        janela.close()

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=FONTE)


def fase_portaria():
    conn = conectar_banco_de_dados()
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) as Total FROM SISREQ WHERE Fase_Processo LIKE '%Portaria%'")
    total_fase_portaria = cursor.fetchone()[0]

    cursor.execute("SELECT * FROM SISREQ WHERE Fase_Processo LIKE '%Portaria%'")
    registros = cursor.fetchall()

    if registros:
        layout = [
            [criar_tabela(registros)],
            [
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de processos: {total_fase_portaria}', font=FONTE_DE_AVSIO)
            ]
        ]

        janela = sg.Window('PROCESSOS EM FASE DE PORTARIA', layout, size=(1200, 700), resizable=True)

        while True:
            event, _ = janela.read()

            if event == sg.WINDOW_CLOSED or event == 'Fechar':
                break

            elif event == 'Extrato':
                salvar_extrato_planilha(registros)

        janela.close()

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=FONTE)


def fase_decreto():
    conn = conectar_banco_de_dados()
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) as Total FROM SISREQ WHERE Fase_Processo LIKE '%Decreto%'")
    total_fase_decreto = cursor.fetchone()[0]

    cursor.execute("SELECT * FROM SISREQ WHERE Fase_Processo LIKE '%Decreto%'")
    registros = cursor.fetchall()

    if registros:
        layout = [
            [criar_tabela(registros)],
            [
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de processos: {total_fase_decreto}', font=FONTE_DE_AVSIO)
            ]
        ]

        janela = sg.Window('ÁREAS DECRETADAS', layout, size=(1200, 700), resizable=True)

        while True:
            event, _ = janela.read()

            if event == sg.WINDOW_CLOSED or event == 'Fechar':
                break

            elif event == 'Extrato':
                salvar_extrato_planilha(registros)

        janela.close()

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=FONTE)


def fase_titulacao():
    conn = conectar_banco_de_dados()
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) as Total FROM SISREQ WHERE Fase_Processo LIKE '%Titulação%'")
    total_fase_titulacao = cursor.fetchone()[0]

    cursor.execute("SELECT * FROM SISREQ WHERE Fase_Processo LIKE '%Titulação%'")
    registros = cursor.fetchall()

    if registros:
        layout = [
            [criar_tabela(registros)],
            [
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de processos: {total_fase_titulacao}', font=FONTE_DE_AVSIO),
                sg.Button('Área Total', button_color='#ac4e04'),
                sg.Button('Número de Famílias', button_color='green'),
            ]
        ]

        janela = sg.Window('PROCESSOS EM FASE DE TITULAÇÃO', layout, size=(1200, 700), resizable=True)

        while True:
            event, _ = janela.read()

            if event == sg.WINDOW_CLOSED or event == 'Fechar':
                break

            elif event == 'Extrato':
                salvar_extrato_planilha(registros)

            elif event == 'Área Total':
                relatorios.exibir_area_total_em_fase_titulacao()

            elif event == 'Número de Famílias':
                relatorios.exibir_total_de_familias_em_fase_titulacao()

        janela.close()

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=FONTE)


def fase_contestacao():
    conn = conectar_banco_de_dados()
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) as Total FROM SISREQ WHERE Fase_Processo LIKE 'Contestação'")
    total_fase_contestacao = cursor.fetchone()[0]
    
    cursor.execute("SELECT * FROM SISREQ WHERE Fase_Processo LIKE '%Contestação%'")
    registros = cursor.fetchall()

    if registros:
        layout = [
            [criar_tabela(registros)],                    
            [
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de processos: {total_fase_contestacao}', font=FONTE_DE_AVSIO)
            ]
        ]

        janela = sg.Window('PROCESSOS EM FASE DE CONTESTAÇÃO', layout, size=(1200, 700), resizable=True)

        while True:
            event, _ = janela.read()

            if event == sg.WINDOW_CLOSED or event == 'Fechar':
                break

            elif event == 'Extrato':
                salvar_extrato_planilha(registros)

        janela.close()

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=FONTE)


def fase_recurso():
    conn = conectar_banco_de_dados()
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) as Total FROM SISREQ WHERE Fase_Processo LIKE '%Recurso%'")
    total_fase_recurso = cursor.fetchone()[0]
    
    cursor.execute("SELECT * FROM SISREQ WHERE Fase_Processo LIKE '%Recurso%'")
    registros = cursor.fetchall()

    if registros:
        layout = [
            [criar_tabela(registros)],
            [
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de processos: {total_fase_recurso}', font=FONTE_DE_AVSIO)
            ]
        ]

        janela = sg.Window('PROCESSOS EM FASE DE RECURSO', layout, size=(1200, 700), resizable=True)

        while True:
            event, _ = janela.read()

            if event == sg.WINDOW_CLOSED or event == 'Fechar':
                break

            elif event == 'Extrato':
                salvar_extrato_planilha(registros)

        janela.close()

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=FONTE)


def fase_desapropriacao():
    conn = conectar_banco_de_dados()
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) as Total FROM SISREQ WHERE Fase_Processo LIKE '%Desapropriação%'")
    total_fase_desapropriacao = cursor.fetchone()[0]

    cursor.execute("SELECT * FROM SISREQ WHERE Fase_Processo LIKE '%Desapropriação%'")
    registros = cursor.fetchall()

    if registros:
        layout = [
            [criar_tabela(registros)],
            [
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de processos: {total_fase_desapropriacao}', font=FONTE_DE_AVSIO)
            ]
        ]
        
        janela = sg.Window('PROCESSOS EM FASE DE DESAPROPRIAÇÃO', layout, size=(1200, 700), resizable=True)

        while True:
            event, _ = janela.read()

            if event == sg.WINDOW_CLOSED or event == 'Fechar':
                break

            elif event == 'Extrato':
                salvar_extrato_planilha(registros)

        janela.close()
        
    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=FONTE)
