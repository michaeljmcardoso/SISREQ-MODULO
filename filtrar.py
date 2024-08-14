import PySimpleGUI as sg
import funcoes_registro
import salvar

def fase_inicial():
    conn = funcoes_registro.conectar_banco_de_dados()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) as Total FROM SISREQ WHERE Fase_Processo LIKE '%Inicial%'")
    totalFaseInicial = cursor.fetchone()[0]

    cursor.execute("SELECT * FROM SISREQ WHERE Fase_Processo LIKE '%Inicial%'")
    registros = cursor.fetchall()

    if registros:
        layoutFaseInicial = [
            [
                sg.Table(
                    values=registros, 
                    headings=[
                            'ID ', 'Numero', 'Data_Abertura', 'Comunidade', 'Municipio', 'Area_ha',
                            'Num_familias', 'Fase_Processo', 'Etapa_RTID', 'Edital_DOU', 'Edital_DOE',
                            'Portaria_DOU', 'Decreto_DOU', 'Área_Titulada_ha', '% Área_Titulada_ha', 'Relatorio_Antropologico',
                            'Latitude', 'Longitude', 'Certidao_FCP', 'Data_Certificacao', 'Sobreposicao',
                            'Analise_de_Sobreposicao', 'Acao_Civil_Publica', 'Data_Decisao', 'Teor_Decisao_Prazo_Sentença',
                            'Outras_Informacoes'
                         ],
                    justification='left', 
                    auto_size_columns=True, 
                    hide_vertical_scroll=False,
                    vertical_scroll_only=False, 
                    num_rows=40)
                    
            ],

            [
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de processos: {totalFaseInicial} Aguardando Início dos Estudos de Identificação e Delimitação', font='Any 10 bold')
            ]

        ]
        janelaInicial = sg.Window('Processos Sem Estudos de Identificação e Delimitação.', layoutFaseInicial, size=(1200, 1200), resizable=True)

        while True:
            event_inicial, _ = janelaInicial.read()

            if event_inicial == sg.WINDOW_CLOSED or event_inicial == 'Fechar':
                break
            elif event_inicial == 'Extrato':
                salvar.extrato_planilha(registros)

        janelaInicial.close()
    else:
        sg.popup('Não há registros para exibir.', title='Erro')

def fase_Rtid():
    conn = funcoes_registro.conectar_banco_de_dados()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) as Total FROM SISREQ WHERE Fase_Processo LIKE '%RTID%'")
    totalFaseRtid = cursor.fetchone()[0]

    cursor.execute("SELECT * FROM SISREQ WHERE Fase_Processo LIKE '%RTID%'")
    registros = cursor.fetchall()

    if registros:
        layoutRtid = [
            [
                sg.Table(
                    values=registros,
                    headings=[
                            'ID ', 'Numero', 'Data_Abertura', 'Comunidade', 'Municipio', 'Area_ha',
                            'Num_familias', 'Fase_Processo', 'Etapa_RTID', 'Edital_DOU', 'Edital_DOE',
                            'Portaria_DOU', 'Decreto_DOU', 'Área_Titulada_ha', '% Área_Titulada_ha', 'Relatorio_Antropologico',
                            'Latitude', 'Longitude', 'Certidao_FCP', 'Data_Certificacao', 'Sobreposicao',
                            'Analise_de_Sobreposicao', 'Acao_Civil_Publica', 'Data_Decisao', 'Teor_Decisao_Prazo_Sentença',
                            'Outras_Informacoes'
                         ],
                    justification='left', 
                    auto_size_columns=True, 
                    hide_vertical_scroll=False,
                    vertical_scroll_only=False, 
                    num_rows=40)
            ],

            [   
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de processos: {totalFaseRtid}', font='Any 10 bold'),
                sg.Text(" "), sg.Button('RTID´s Publicados', button_color='blue')
            ]
        ]

        janelaRtid = sg.Window('Processos em Estudo de Identificação e Delimitação', layoutRtid, size=(1200, 1200), resizable=True)

        while True:
            event_rtid, _ = janelaRtid.read()

            if event_rtid == sg.WINDOW_CLOSED or event_rtid == 'Fechar':
                break
            elif event_rtid == 'Extrato':
                salvar.extrato_planilha(registros)
            elif event_rtid == 'RTID´s Publicados':
                rtidsPublicados()
        janelaRtid.close()
    else:
        sg.popup('Não há registros para exibir.', title='Erro')


def rtidsPublicados():
    conn = funcoes_registro.conectar_banco_de_dados()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) as Total FROM SISREQ WHERE Edital_DOU")
    totalRtidPublicado = cursor.fetchone()[0]

    cursor.execute("SELECT * FROM SISREQ WHERE  Edital_DOU")
    registros = cursor.fetchall()

    if registros:
        layoutRtidPublicado = [
            [
                sg.Table(
                    values=registros,
                    headings=[
                            'ID ', 'Numero', 'Data_Abertura', 'Comunidade', 'Municipio', 'Area_ha',
                            'Num_familias', 'Fase_Processo', 'Etapa_RTID', 'Edital_DOU', 'Edital_DOE',
                            'Portaria_DOU', 'Decreto_DOU', 'Área_Titulada_ha', '% Área_Titulada_ha', 'Relatorio_Antropologico',
                            'Latitude', 'Longitude', 'Certidao_FCP', 'Data_Certificacao', 'Sobreposicao',
                            'Analise_de_Sobreposicao', 'Acao_Civil_Publica', 'Data_Decisao', 'Teor_Decisao_Prazo_Sentença',
                            'Outras_Informacoes'
                         ],
                    justification='left', 
                    auto_size_columns=True, 
                    hide_vertical_scroll=False,
                    vertical_scroll_only=False, 
                    num_rows=40)
            ],

            [
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de RTID´s Publicados: {totalRtidPublicado}', font='Any 10 bold'),
                sg.Button('Área Identificada', button_color='#ac4e04'),
                sg.Button('Número de Famílias', button_color='green')
            ]

            ]

        janelaRtidPublicado = sg.Window('Relatórios Publicados', layoutRtidPublicado, size=(1200, 1200), resizable=True)

        while True:
            event_publicado, _ = janelaRtidPublicado.read()

            if event_publicado == sg.WINDOW_CLOSED or event_publicado == 'Fechar':
                break
            elif event_publicado == 'Extrato':
                salvar.extrato_planilha(registros)
            elif event_publicado == 'Número de Famílias':
                contarNumeroDeFamiliasEmRelatoriosPublicados()
            elif event_publicado == 'Área Identificada':
                contarAreaRtidPublicado()


        janelaRtidPublicado.close()
    else:
        sg.popup('Não há registros para exibir.', title='Erro')


def fase_publicacao():
    conn = funcoes_registro.conectar_banco_de_dados()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) as Total FROM SISREQ WHERE Fase_Processo LIKE '%Publicação%'")
    totalFasePublicacao = cursor.fetchone()[0]

    cursor.execute("SELECT * FROM SISREQ WHERE Fase_Processo LIKE '%Publicação%'")
    registros = cursor.fetchall()

    if registros:
        layout_publicacao = [
            [
                sg.Table(
                    values=registros,
                    headings=[
                            'ID ', 'Numero', 'Data_Abertura', 'Comunidade', 'Municipio', 'Area_ha',
                            'Num_familias', 'Fase_Processo', 'Etapa_RTID', 'Edital_DOU', 'Edital_DOE',
                            'Portaria_DOU', 'Decreto_DOU', 'Área_Titulada_ha', '% Área_Titulada_ha', 'Relatorio_Antropologico',
                            'Latitude', 'Longitude', 'Certidao_FCP', 'Data_Certificacao', 'Sobreposicao',
                            'Analise_de_Sobreposicao', 'Acao_Civil_Publica', 'Data_Decisao', 'Teor_Decisao_Prazo_Sentença',
                            'Outras_Informacoes'
                         ],
                    justification='left', 
                    auto_size_columns=True, 
                    hide_vertical_scroll=False,
                    vertical_scroll_only=False, 
                    num_rows=40)
            ],

            [
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de processos: {totalFasePublicacao}', font='Any 10 bold')
            ]

        ]

        janelaPublicacao = sg.Window('Processos em Fase de Publicação', layout_publicacao, size=(1200, 1200),
                                      resizable=True)

        while True:
            event_publicacao, _ = janelaPublicacao.read()

            if event_publicacao == sg.WINDOW_CLOSED or event_publicacao == 'Fechar':
                break
            elif event_publicacao == 'Extrato':
                salvar.extrato_planilha(registros)
        janelaPublicacao.close()
    else:
        sg.popup('Não há registros para exibir.', title='Erro')

def fase_notificacao():
    conn = funcoes_registro.conectar_banco_de_dados()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) as Total FROM SISREQ WHERE Fase_Processo LIKE '%Notificação%'")
    total_fase_notificacao = cursor.fetchone()[0]

    cursor.execute("SELECT * FROM SISREQ WHERE Fase_Processo LIKE '%Notificação%'")
    registros = cursor.fetchall()

    if registros:
        layout_notificacao = [
            [
                sg.Table(
                    values=registros,
                    headings=[
                            'ID ', 'Numero', 'Data_Abertura', 'Comunidade', 'Municipio', 'Area_ha',
                            'Num_familias', 'Fase_Processo', 'Etapa_RTID', 'Edital_DOU', 'Edital_DOE',
                            'Portaria_DOU', 'Decreto_DOU', 'Área_Titulada_ha', '% Área_Titulada_ha', 'Relatorio_Antropologico',
                            'Latitude', 'Longitude', 'Certidao_FCP', 'Data_Certificacao', 'Sobreposicao',
                            'Analise_de_Sobreposicao', 'Acao_Civil_Publica', 'Data_Decisao', 'Teor_Decisao_Prazo_Sentença',
                            'Outras_Informacoes'
                         ],
                    justification='left', 
                    auto_size_columns=True, 
                    hide_vertical_scroll=False,
                    vertical_scroll_only=False, 
                    num_rows=40)
            ],

            [
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de processos: {total_fase_notificacao}', font='Any 10 bold')
            ]

        ]

        janelaNotificacao = sg.Window('Processos em Fase de Notificação', layout_notificacao, size=(1200, 1200), resizable=True)

        while True:
            event_notificacao, _ = janelaNotificacao.read()

            if event_notificacao == sg.WINDOW_CLOSED or event_notificacao == 'Fechar':
                break
            elif event_notificacao == 'Extrato':
                salvar.extrato_planilha(registros)
        janelaNotificacao.close()
    else:
        sg.popup('Não há registros para exibir.', title='Erro')


def fase_portaria():
    conn = funcoes_registro.conectar_banco_de_dados()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) as Total FROM SISREQ WHERE Fase_Processo LIKE '%Portaria%'")
    total_fase_portaria = cursor.fetchone()[0]

    cursor.execute("SELECT * FROM SISREQ WHERE Fase_Processo LIKE '%Portaria%'")
    registros = cursor.fetchall()

    if registros:
        layout_portaria = [
            [
                sg.Table(
                    values=registros, 
                    headings=[
                            'ID ', 'Numero', 'Data_Abertura', 'Comunidade', 'Municipio', 'Area_ha',
                            'Num_familias', 'Fase_Processo', 'Etapa_RTID', 'Edital_DOU', 'Edital_DOE',
                            'Portaria_DOU', 'Decreto_DOU', 'Área_Titulada_ha', '% Área_Titulada_ha', 'Relatorio_Antropologico',
                            'Latitude', 'Longitude', 'Certidao_FCP', 'Data_Certificacao', 'Sobreposicao',
                            'Analise_de_Sobreposicao', 'Acao_Civil_Publica', 'Data_Decisao', 'Teor_Decisao_Prazo_Sentença',
                            'Outras_Informacoes'
                         ],
                    justification='left', 
                    auto_size_columns=True, 
                    hide_vertical_scroll=False,
                    vertical_scroll_only=False, 
                    num_rows=40)
            ],

            [
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de processos: {total_fase_portaria}', font='Any 10 bold')
            ]

        ]
        window_portaria = sg.Window('Processos em Fase de Portaria', layout_portaria, size=(1200, 1200), resizable=True)

        while True:
            event_portaria, _ = window_portaria.read()

            if event_portaria == sg.WINDOW_CLOSED or event_portaria == 'Fechar':
                break
            elif event_portaria == 'Extrato':
                salvar.extrato_planilha(registros)
        window_portaria.close()

    else:
        sg.popup('Não há registros para exibir.', title='Erro')


def fase_decreto():
    conn = funcoes_registro.conectar_banco_de_dados()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) as Total FROM SISREQ WHERE Fase_Processo LIKE '%Decreto%'")
    total_fase_decreto = cursor.fetchone()[0]

    cursor.execute("SELECT * FROM SISREQ WHERE Fase_Processo LIKE '%Decreto%'")
    registros = cursor.fetchall()

    if registros:
        layout_decreto = [
            [
                sg.Table(
                    values=registros, 
                    headings=[
                            'ID ', 'Numero', 'Data_Abertura', 'Comunidade', 'Municipio', 'Area_ha',
                            'Num_familias', 'Fase_Processo', 'Etapa_RTID', 'Edital_DOU', 'Edital_DOE',
                            'Portaria_DOU', 'Decreto_DOU', 'Área_Titulada_ha', '% Área_Titulada_ha', 'Relatorio_Antropologico',
                            'Latitude', 'Longitude', 'Certidao_FCP', 'Data_Certificacao', 'Sobreposicao',
                            'Analise_de_Sobreposicao', 'Acao_Civil_Publica', 'Data_Decisao', 'Teor_Decisao_Prazo_Sentença',
                            'Outras_Informacoes'
                         ],
                    justification='left', 
                    auto_size_columns=True, 
                    hide_vertical_scroll=False,
                    vertical_scroll_only=False, 
                    num_rows=40)
            ],

            [
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de processos: {total_fase_decreto}', font='Any 10 bold')
            ]

        ]
        window_decreto = sg.Window('Áreas Decretadas', layout_decreto, size=(1200, 1200), resizable=True)

        while True:
            event_decreto, _ = window_decreto.read()

            if event_decreto == sg.WINDOW_CLOSED or event_decreto == 'Fechar':
                break
            elif event_decreto == 'Extrato':
                salvar.extrato_planilha(registros)

        window_decreto.close()

    else:
        sg.popup('Não há registros para exibir.', title='Erro')


def fase_titulacao():
    conn = funcoes_registro.conectar_banco_de_dados()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) as Total FROM SISREQ WHERE Fase_Processo LIKE '%Titulação%'")
    total_fase_titulacao = cursor.fetchone()[0]

    cursor.execute("SELECT * FROM SISREQ WHERE Fase_Processo LIKE '%Titulação%'")
    registros = cursor.fetchall()

    if registros:
        layout_titulacao = [
            [
                sg.Table(
                   values=registros, 
                   headings=[
                            'ID ', 'Numero', 'Data_Abertura', 'Comunidade', 'Municipio', 'Area_ha',
                            'Num_familias', 'Fase_Processo', 'Etapa_RTID', 'Edital_DOU', 'Edital_DOE',
                            'Portaria_DOU', 'Decreto_DOU', 'Área_Titulada_ha', '% Área_Titulada_ha', 'Relatorio_Antropologico',
                            'Latitude', 'Longitude', 'Certidao_FCP', 'Data_Certificacao', 'Sobreposicao',
                            'Analise_de_Sobreposicao', 'Acao_Civil_Publica', 'Data_Decisao', 'Teor_Decisao_Prazo_Sentença',
                            'Outras_Informacoes'
                         ],
                    justification='left', 
                    auto_size_columns=True, 
                    hide_vertical_scroll=False,
                    vertical_scroll_only=False, 
                    num_rows=40)
            ],

            [
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de processos: {total_fase_titulacao}', font='Any 10 bold'),
                sg.Button('Área Total', button_color='#ac4e04'),
                sg.Button('Número de Famílias', button_color='green'),
                sg.Button('Titulos Expedidos', button_color='blue')
            ]
        ]
        window_titulacao = sg.Window('Processos em Fase de Titulação', layout_titulacao, size=(1200, 1200), resizable=True)

        while True:
            event_titulacao, _ = window_titulacao.read()

            if event_titulacao == sg.WINDOW_CLOSED or event_titulacao == 'Fechar':
                break
            elif event_titulacao == 'Extrato':
                salvar.extrato_planilha(registros)
            elif event_titulacao == 'Área Total':
                contar_e_apresentar_area_fase_titulacao()
            elif event_titulacao == 'Número de Famílias':
                contarFamiliasEmFaseTitulacao()
            elif event_titulacao == 'Titulos Expedidos':
                titulos_expedidos()

        window_titulacao.close()
    else:
        sg.popup('Não há registros para exibir.', title='Erro')


def titulos_expedidos():
    conn = funcoes_registro.conectar_banco_de_dados()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) as Total FROM SISREQ WHERE Titulo")
    total_titulos_expedidos = cursor.fetchone()[0]

    cursor.execute("SELECT * FROM SISREQ WHERE Titulo")
    registros = cursor.fetchall()

    if registros:
        layout_titulado = [
            [
                sg.Table(
                    values=registros,
                    headings=[
                            'ID ', 'Numero', 'Data_Abertura', 'Comunidade', 'Municipio', 'Area_ha',
                            'Num_familias', 'Fase_Processo', 'Etapa_RTID', 'Edital_DOU', 'Edital_DOE',
                            'Portaria_DOU', 'Decreto_DOU', 'Área_Titulada_ha', '% Área_Titulada_ha', 'Relatorio_Antropologico',
                            'Latitude', 'Longitude', 'Certidao_FCP', 'Data_Certificacao', 'Sobreposicao',
                            'Analise_de_Sobreposicao', 'Acao_Civil_Publica', 'Data_Decisao', 'Teor_Decisao_Prazo_Sentença',
                            'Outras_Informacoes'
                         ],
                    justification='left', 
                    auto_size_columns=True, 
                    hide_vertical_scroll=False,
                    vertical_scroll_only=False, 
                    num_rows=40)
            ],

            [
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de processos: {total_titulos_expedidos}', font='Any 10 bold'),
                sg.Button('Área Total', button_color='#ac4e04'),
                sg.Button('Número de Famílias', button_color='green')
            ]
        ]
        window_titulado = sg.Window('Títulos Expedidos', layout_titulado, size=(1200, 1200), resizable=True)

        while True:
            event_titulado, _ = window_titulado.read()

            if event_titulado == sg.WINDOW_CLOSED or event_titulado == 'Fechar':
                break
            elif event_titulado == 'Extrato':
                salvar.extrato_planilha(registros)
            elif event_titulado == 'Área Total':
                contar_e_apresentar_area_titulada()
            elif event_titulado == 'Número de Famílias':
                contar_e_apresentar_familias_tituladas()

        window_titulado.close()
    else:
        sg.popup('Não há registros para exibir.', title='Erro')


def fase_desintrusao():
    conn = funcoes_registro.conectar_banco_de_dados()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) as Total FROM SISREQ WHERE Fase_Processo LIKE '%Desintrusão%'")
    total_fase_desintrusao = cursor.fetchone()[0]

    cursor.execute("SELECT * FROM SISREQ WHERE Fase_Processo LIKE '%Desintrusão%'")
    registros = cursor.fetchall()

    if registros:
        layout_desintrusao = [
            [
                sg.Table(
                    values=registros,
                    headings=[
                            'ID ', 'Numero', 'Data_Abertura', 'Comunidade', 'Municipio', 'Area_ha',
                            'Num_familias', 'Fase_Processo', 'Etapa_RTID', 'Edital_DOU', 'Edital_DOE',
                            'Portaria_DOU', 'Decreto_DOU', 'Área_Titulada_ha', '% Área_Titulada_ha', 'Relatorio_Antropologico',
                            'Latitude', 'Longitude', 'Certidao_FCP', 'Data_Certificacao', 'Sobreposicao',
                            'Analise_de_Sobreposicao', 'Acao_Civil_Publica', 'Data_Decisao', 'Teor_Decisao_Prazo_Sentença',
                            'Outras_Informacoes'
                         ],
                    justification='left', 
                    auto_size_columns=True, 
                    hide_vertical_scroll=False,
                    vertical_scroll_only=False, 
                    num_rows=40)
            ],

            [
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de processos: {total_fase_desintrusao}', font='Any 10 bold')
            ]

        ]
        window_desintrusao = sg.Window('Processos em Fase de Desintrusão', layout_desintrusao, size=(1200, 1200), resizable=True)

        while True:
            event_desintrusao, _ = window_desintrusao.read()

            if event_desintrusao == sg.WINDOW_CLOSED or event_desintrusao == 'Fechar':
                break
            elif event_desintrusao == 'Extrato':
                salvar.extrato_planilha(registros)
        window_desintrusao.close()

    else:
        sg.popup('Não há registros para exibir.', title='Erro')


def fase_contestacao():
    conn = funcoes_registro.conectar_banco_de_dados()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) as Total FROM SISREQ WHERE Fase_Processo LIKE 'Contestação'")
    total_fase_contestacao = cursor.fetchone()[0]
    
    cursor.execute("SELECT * FROM SISREQ WHERE Fase_Processo LIKE '%Contestação%'")
    registros = cursor.fetchall()

    if registros:
        layout_contestacao = [
            [
                sg.Table(
                    values=registros, 
                    headings=[
                            'ID ', 'Numero', 'Data_Abertura', 'Comunidade', 'Municipio', 'Area_ha',
                            'Num_familias', 'Fase_Processo', 'Etapa_RTID', 'Edital_DOU', 'Edital_DOE',
                            'Portaria_DOU', 'Decreto_DOU', 'Área_Titulada_ha', '% Área_Titulada_ha', 'Relatorio_Antropologico',
                            'Latitude', 'Longitude', 'Certidao_FCP', 'Data_Certificacao', 'Sobreposicao',
                            'Analise_de_Sobreposicao', 'Acao_Civil_Publica', 'Data_Decisao', 'Teor_Decisao_Prazo_Sentença',
                            'Outras_Informacoes'
                         ],
                    justification='left', 
                    auto_size_columns=True, 
                    hide_vertical_scroll=False,
                    vertical_scroll_only=False, 
                    num_rows=40)
            ],
                    
            [
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de processos: {total_fase_contestacao}', font='Any 10 bold')
            ]
            
        ]
        window_contestacao = sg.Window('Processos em Fase de Contestação', layout_contestacao, size=(1200, 1200), resizable=True)

        while True:
            event_contestacao, _ = window_contestacao.read()

            if event_contestacao == sg.WINDOW_CLOSED or event_contestacao == 'Fechar':
                break
            elif event_contestacao == 'Extrato':
                salvar.extrato_planilha(registros)

        window_contestacao.close()
    else:
        sg.popup('Não há registros para exibir.', title='Erro')


def fase_recurso():
    conn = funcoes_registro.conectar_banco_de_dados()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) as Total FROM SISREQ WHERE Fase_Processo LIKE '%Recurso%'")
    total_fase_recurso = cursor.fetchone()[0]
    
    cursor.execute("SELECT * FROM SISREQ WHERE Fase_Processo LIKE '%Recurso%'")
    registros = cursor.fetchall()

    if registros:
        layout_recurso = [
            [
                sg.Table(values=registros,
                      headings=[
                            'ID ', 'Numero', 'Data_Abertura', 'Comunidade', 'Municipio', 'Area_ha',
                            'Num_familias', 'Fase_Processo', 'Etapa_RTID', 'Edital_DOU', 'Edital_DOE',
                            'Portaria_DOU', 'Decreto_DOU', 'Área_Titulada_ha', '% Área_Titulada_ha', 'Relatorio_Antropologico',
                            'Latitude', 'Longitude', 'Certidao_FCP', 'Data_Certificacao', 'Sobreposicao',
                            'Analise_de_Sobreposicao', 'Acao_Civil_Publica', 'Data_Decisao', 'Teor_Decisao_Prazo_Sentença',
                            'Outras_Informacoes'
                         ],
                    justification='left', 
                    auto_size_columns=True, 
                    hide_vertical_scroll=False,
                    vertical_scroll_only=False, 
                    num_rows=40)
            ],

            [
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de processos: {total_fase_recurso}', font='Any 10 bold')
            ]

        ]
        window_recurso = sg.Window('Processos em Fase de Recurso', layout_recurso, size=(1200, 1200), resizable=True)

        while True:
            event_recurso, _ = window_recurso.read()

            if event_recurso == sg.WINDOW_CLOSED or event_recurso == 'Fechar':
                break
            elif event_recurso == 'Extrato':
                salvar.extrato_planilha(registros)

        window_recurso.close()
    else:
        sg.popup('Não há registros para exibir.', title='Erro')


def fase_desapropriacao():
    conn = funcoes_registro.conectar_banco_de_dados()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) as Total FROM SISREQ WHERE Fase_Processo LIKE '%Desapropriação%'")
    total_fase_desapropriacao = cursor.fetchone()[0]

    cursor.execute("SELECT * FROM SISREQ WHERE Fase_Processo LIKE '%Desapropriação%'")
    registros = cursor.fetchall()

    if registros:
        layout_desapropriacao = [
            [
                sg.Table(
                      values=registros,
                      headings=[
                            'ID ', 'Numero', 'Data_Abertura', 'Comunidade', 'Municipio', 'Area_ha',
                            'Num_familias', 'Fase_Processo', 'Etapa_RTID', 'Edital_DOU', 'Edital_DOE',
                            'Portaria_DOU', 'Decreto_DOU', 'Área_Titulada_ha', '% Área_Titulada_ha', 'Relatorio_Antropologico',
                            'Latitude', 'Longitude', 'Certidao_FCP', 'Data_Certificacao', 'Sobreposicao',
                            'Analise_de_Sobreposicao', 'Acao_Civil_Publica', 'Data_Decisao', 'Teor_Decisao_Prazo_Sentença',
                            'Outras_Informacoes'
                        ],
                      justification='left', 
                      auto_size_columns=True, 
                      hide_vertical_scroll=False,
                      vertical_scroll_only=False, 
                      num_rows=40)
            ],

            [
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de processos: {total_fase_desapropriacao}', font='Any 10 bold')
            ]

        ]
        window_desapropriacao = sg.Window('Processos em Fase de Desapropriação', layout_desapropriacao, size=(1200, 1200), resizable=True)

        while True:
            event_desapropriacao, _ = window_desapropriacao.read()

            if event_desapropriacao == sg.WINDOW_CLOSED or event_desapropriacao == 'Fechar':
                break
            elif event_desapropriacao == 'Extrato':
                salvar.extrato_planilha(registros)

        window_desapropriacao.close()
    else:
        sg.popup('Não há registros para exibir.', title='Erro')