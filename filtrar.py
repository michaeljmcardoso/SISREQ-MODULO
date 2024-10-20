import PySimpleGUI as sg
import relatorios
from funcoes_registro import conectar_banco_de_dados
from salvar import salvar_extrato_planilha
from constantes import FONTE
from constantes import headings

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
            [
                sg.Table(
                    values=registros, 
                    headings=headings,
                    justification='left', 
                    auto_size_columns=True, 
                    hide_vertical_scroll=False,
                    vertical_scroll_only=False, 
                    num_rows=35)
                    
            ],

            [
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de processos: {total_fase_inicial} Aguardando Início dos Estudos de Identificação e Delimitação', font='Any 10 bold')
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
    
    cursor.execute("SELECT COUNT(*) as Total FROM SISREQ WHERE Fase_Processo LIKE '%RTID%'")
    total_fase_rtid = cursor.fetchone()[0]

    cursor.execute("SELECT * FROM SISREQ WHERE Fase_Processo LIKE '%RTID%'")
    registros = cursor.fetchall()

    if registros:
        layout = [
            [
                sg.Table(
                    values=registros,
                    headings=headings,
                    justification='left', 
                    auto_size_columns=True, 
                    hide_vertical_scroll=False,
                    vertical_scroll_only=False, 
                    num_rows=35)
            ],

            [   
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de processos: {total_fase_rtid}', font='Any 10 bold'),
                
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
            [
                sg.Table(
                    values=registros,
                    headings=headings,
                    justification='left', 
                    auto_size_columns=True, 
                    hide_vertical_scroll=False,
                    vertical_scroll_only=False, 
                    num_rows=35)
            ],

            [
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de processos: {total_fase_publicacao}', font='Any 10 bold')
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
            [
                sg.Table(
                    values=registros,
                    headings=headings,
                    justification='left', 
                    auto_size_columns=True, 
                    hide_vertical_scroll=False,
                    vertical_scroll_only=False, 
                    num_rows=35)
            ],

            [
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de processos: {total_fase_notificacao}', font='Any 10 bold')
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
            [
                sg.Table(
                    values=registros, 
                    headings=headings,
                    justification='left', 
                    auto_size_columns=True, 
                    hide_vertical_scroll=False,
                    vertical_scroll_only=False, 
                    num_rows=35)
            ],

            [
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de processos: {total_fase_portaria}', font='Any 10 bold')
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
            [
                sg.Table(
                    values=registros, 
                    headings=headings,
                    justification='left', 
                    auto_size_columns=True, 
                    hide_vertical_scroll=False,
                    vertical_scroll_only=False, 
                    num_rows=35)
            ],

            [
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de processos: {total_fase_decreto}', font='Any 10 bold')
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
            [
                sg.Table(
                   values=registros, 
                   headings=headings,
                    justification='left', 
                    auto_size_columns=True, 
                    hide_vertical_scroll=False,
                    vertical_scroll_only=False, 
                    num_rows=35)
            ],

            [
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de processos: {total_fase_titulacao}', font='Any 10 bold'),
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


def fase_desintrusao():
    conn = conectar_banco_de_dados()
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) as Total FROM SISREQ WHERE Fase_Processo LIKE '%Desintrusão%'")
    total_fase_desintrusao = cursor.fetchone()[0]

    cursor.execute("SELECT * FROM SISREQ WHERE Fase_Processo LIKE '%Desintrusão%'")
    registros = cursor.fetchall()

    if registros:
        layout = [
            [
                sg.Table(
                    values=registros,
                    headings=headings,
                    justification='left', 
                    auto_size_columns=True, 
                    hide_vertical_scroll=False,
                    vertical_scroll_only=False, 
                    num_rows=35)
            ],

            [
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de processos: {total_fase_desintrusao}', font='Any 10 bold')
            ]

        ]

        janela = sg.Window('PROCESSOS EM FASE DE DESINTRUSÃO', layout, size=(1200, 700), resizable=True)

        while True:
            event, _ = janela.read()

            if event == sg.WINDOW_CLOSED or event == 'Fechar':
                break

            elif event == 'Extrato':
                salvar_extrato_planilha(registros)

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
            [
                sg.Table(
                    values=registros, 
                    headings=headings,
                    justification='left', 
                    auto_size_columns=True, 
                    hide_vertical_scroll=False,
                    vertical_scroll_only=False, 
                    num_rows=35)
            ],
                    
            [
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de processos: {total_fase_contestacao}', font='Any 10 bold')
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
            [
                sg.Table(
                    values=registros,
                    headings=[
                        'ID ', 'Numero', 'Data_Abertura', 'Comunidade', 'Municipio', 'Area_ha',
                        'Num_familias', 'Fase_Processo', 'Etapa_RTID', 'Edital_DOU', 'Edital_DOE',
                        'Portaria_DOU', 'Decreto_DOU', 'Área_Titulada_ha', '  PNRA   ', 'Relatorio_Antropologico',
                        'Latitude', 'Longitude', 'Certidao_FCP', 'Data_Certificacao', 'Sobreposicao',
                        'Analise_de_Sobreposicao', 'Acao_Civil_Publica', 'Data_Decisao', 'Teor_Decisao_Prazo_Sentença',
                        'Outras_Informacoes'
                    ],
                    justification='left', 
                    auto_size_columns=True, 
                    hide_vertical_scroll=False,
                    vertical_scroll_only=False, 
                    num_rows=35)
            ],

            [
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de processos: {total_fase_recurso}', font='Any 10 bold')
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
            [
                sg.Table(
                    values=registros,
                    headings=[
                        'ID ', 'Numero', 'Data_Abertura', 'Comunidade', 'Municipio', 'Area_ha',
                        'Num_familias', 'Fase_Processo', 'Etapa_RTID', 'Edital_DOU', 'Edital_DOE',
                        'Portaria_DOU', 'Decreto_DOU', 'Área_Titulada_ha', '  PNRA   ', 'Relatorio_Antropologico',
                        'Latitude', 'Longitude', 'Certidao_FCP', 'Data_Certificacao', 'Sobreposicao',
                        'Analise_de_Sobreposicao', 'Acao_Civil_Publica', 'Data_Decisao', 'Teor_Decisao_Prazo_Sentença',
                        'Outras_Informacoes'
                    ],
                    justification='left', 
                    auto_size_columns=True, 
                    hide_vertical_scroll=False,
                    vertical_scroll_only=False, 
                    num_rows=35)
            ],

            [
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de processos: {total_fase_desapropriacao}', font='Any 10 bold')
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
