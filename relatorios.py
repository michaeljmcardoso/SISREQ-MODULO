import PySimpleGUI as sg
import funcoes_registro
import salvar
import constantes

"""Funções para exibir relatórios em tabelas"""

def rtids_publicados():
    conn = funcoes_registro.conectar_banco_de_dados()
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) as Total FROM SISREQ WHERE Edital_DOU")
    totalRtidPublicado = cursor.fetchone()[0]

    cursor.execute("SELECT * FROM SISREQ WHERE  Edital_DOU")
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

        janela = sg.Window('Relatórios Publicados', layout, size=(1200, 1200), resizable=True)

        while True:
            event, _ = janela.read()

            if event == sg.WINDOW_CLOSED or event == 'Fechar':
                break

            elif event == 'Extrato':
                salvar.extrato_planilha(registros)

            elif event == 'Número de Famílias':
                exibir_total_de_familias_em_rtids_publicados()

            elif event == 'Área Identificada':
                exibir_area_total_em_rtids_publicados()

        janela.close()

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=constantes.FONTE)


def titulos_expedidos():
    conn = funcoes_registro.conectar_banco_de_dados()
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) as Total FROM SISREQ WHERE Area_ha_Titulada")
    total_titulos_expedidos = cursor.fetchone()[0]

    cursor.execute("SELECT * FROM SISREQ WHERE Area_ha_Titulada")
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

        janela = sg.Window('Títulos Expedidos', layout, size=(1200, 1200), resizable=True)

        while True:
            event, _ = janela.read()

            if event == sg.WINDOW_CLOSED or event == 'Fechar':
                break

            elif event == 'Extrato':
                salvar.extrato_planilha(registros)

            elif event == 'Área Total':
                exibir_area_total_em_areas_tituladas()

            elif event == 'Número de Famílias':
                exibir_total_de_familias_em_areas_tituladas()

        janela.close()

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=constantes.FONTE)


def territorios_identificados():
    conn = funcoes_registro.conectar_banco_de_dados()
    cursor = conn.cursor()
    
    cursor.execute(
        "SELECT COUNT(*) FROM SISREQ WHERE "
        "Relatorio_Antropologico LIKE '%Execução_Direta%' OR "
        "Relatorio_Antropologico LIKE '%Contrato%' OR "
        "Relatorio_Antropologico LIKE '%Doação%' OR "
        "Relatorio_Antropologico LIKE '%Acordo_Coop_Técnica%' OR "
        "Relatorio_Antropologico LIKE '%Termo_Execução_Descentralizada%' "
        )
    
    total_de_territorios_identificados = cursor.fetchone()[0]

    cursor.execute(
        "SELECT * FROM SISREQ WHERE "
        "Relatorio_Antropologico LIKE '%Execução_Direta%' OR "
        "Relatorio_Antropologico LIKE '%Contrato%' OR "
        "Relatorio_Antropologico LIKE '%Doação%' OR "
        "Relatorio_Antropologico LIKE '%Acordo_Coop_Técnica%' OR "
        "Relatorio_Antropologico LIKE '%Termo_Execução_Descentralizada%' "
    )

    registros = cursor.fetchall()

    if registros:
        layout = [
            [
                sg.Table(
                    values=registros,
                    headings=[
                        'ID ', '    Numero   ', 'Data_Abertura', '  Comunidade  ', '  Municipio  ', ' Area_ha ',
                        'Num_familias', 'Fase_Processo', ' Etapa_RTID ', ' Edital_DOU ', 'Edital_DOE',
                        'Portaria_DOU', 'Decreto_DOU', 'Area_ha_Titulada', '  PNRA   ', 'Relatorio_Antropologico',
                        'Latitude', 'Longitude', 'Certidao_FCP', 'Data_Certificacao', '  Sobreposicao  ',
                        'Analise_de_Sobreposicao', 'Acao_Civil_Publica', 'Data_Decisao', 'Teor_Decisao_Prazo_Sentença',
                        '          Outras_Informacoes'
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
                sg.Text(f'Total de Processos: {total_de_territorios_identificados} registros encontrados com Território Identificado', font='Any 10 bold'),
                sg.Button('Área Identificada', button_color='#ac4e04'),
                sg.Button('Número de Famílias', button_color='green'),
            ]
        ]

        janela = sg.Window('Territórios Identificados', layout, size=(1200, 1200), resizable=True)

        while True:
            event, _ = janela.read()

            if event == sg.WINDOW_CLOSED or event == 'Fechar':
                break

            elif event == 'Extrato':
                salvar.extrato_planilha(registros)

            elif event == 'Número de Famílias':
                exibir_total_de_familias_em_territorios_identificados()

            elif event == 'Área Identificada':
                exibir_area_total_em_territorios_identificados()

        janela.close()

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=constantes.FONTE)


def territorios_nao_identificados():
    conn = funcoes_registro.conectar_banco_de_dados()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM SISREQ WHERE Relatorio_Antropologico LIKE '%Sem_Relatório%'")
    registros = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) FROM SISREQ WHERE Relatorio_Antropologico LIKE '%Sem_Relatório%'")
    total_de_territorios_nao_identificados = cursor.fetchone()[0]

    if registros:
        layout = [
            [
                sg.Table(
                        values=registros, 
                        headings=[
                            'ID ', '    Numero   ', 'Data_Abertura', '  Comunidade  ', '  Municipio  ', ' Area_ha ',
                            'Num_familias', 'Fase_Processo', ' Etapa_RTID ', ' Edital_DOU ', 'Edital_DOE',
                            'Portaria_DOU', 'Decreto_DOU', 'Area_ha_Titulada', '  PNRA   ', 'Relatorio_Antropologico',
                            'Latitude', 'Longitude', 'Certidao_FCP', 'Data_Certificacao', '  Sobreposicao  ',
                            'Analise_de_Sobreposicao', 'Acao_Civil_Publica', 'Data_Decisao', 'Teor_Decisao_Prazo_Sentença',
                            '          Outras_Informacoes'
                        ],
                        justification='left', 
                        auto_size_columns=True, 
                        hide_vertical_scroll=False,
                        vertical_scroll_only=False, 
                        num_rows=40
                    )
            ],

            [
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de Processos: {total_de_territorios_nao_identificados} Território(s) Não Identificado(s)', font='Any 10 bold'),
            ]

        ]

        janela = sg.Window('Territórios Não-Identificados', layout, size=(1200, 1200), resizable=True)

        while True:
            event, _ = janela.read()

            if event == sg.WINDOW_CLOSED or event == 'Fechar':
                break

            elif event == 'Extrato':
                salvar.extrato_planilha(registros)

        janela.close()

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=constantes.FONTE)


def exibir_territorios_quilombolas_em_assentamentos():
    conn = funcoes_registro.conectar_banco_de_dados()
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM SISREQ WHERE Sobreposicao LIKE '%PA_INCRA%' OR Sobreposicao LIKE '%PA_ITERMA%'")
    total_territorio_quilombola_em_assentamento = cursor.fetchone()[0]

    cursor.execute("SELECT * FROM SISREQ WHERE Sobreposicao LIKE '%PA_INCRA%' OR Sobreposicao LIKE '%PA_ITERMA%'")
    registros = cursor.fetchall()

    if registros:
        layout = [
            [
                sg.Table(
                    values=registros, 
                    headings=[
                        'ID', 'Numero', 'Data_Abertura', 'Comunidade', 'Municipio', 'Area_ha',
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
                    num_rows=40)
            ],
            
            [sg.Button('Fechar', button_color='#ac4e04'), sg.Button('Extrato', button_color='green'), sg.Text(f'Total de processos: {total_territorio_quilombola_em_assentamento} registros encontrados de comunidades quilombolas em projetos de assentamento.', font='Any 10 bold')]
        ]

        janela = sg.Window('Territórios Quilombolas em Projetos de Assentamento', layout, size=(1200, 1200), resizable=True)

        while True:
            event, _ = janela.read()

            if event == sg.WINDOW_CLOSED or event == 'Fechar':
                break

            elif event == 'Extrato':
                salvar.extrato_planilha(registros)

        janela.close()

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=constantes.FONTE)


def exibir_processos_com_acao_judicial():
    conn = funcoes_registro.conectar_banco_de_dados()
    cursor = conn.cursor()
    
    cursor.execute(
        "SELECT COUNT(*) FROM SISREQ WHERE "
        "Acao_Civil_Publica LIKE '%Com_Sentença%' OR "
        "Acao_Civil_Publica LIKE '%Com_Decisão_Liminar%' OR "
        "Acao_Civil_Publica LIKE '%Corte_InterAmericana%' OR "
        "Acao_Civil_Publica LIKE '%Sem_Sentença%' OR "
        "Acao_Civil_Publica LIKE '%Sentença_Cumprida%'"
    )
    
    total_acao_civil = cursor.fetchone()[0]

    cursor.execute(
        "SELECT * FROM SISREQ WHERE "
        "Acao_Civil_Publica LIKE '%Com_Sentença%' OR "
        "Acao_Civil_Publica LIKE '%Com_Decisão_Liminar%' OR "
        "Acao_Civil_Publica LIKE '%Corte_InterAmericana%' OR "
        "Acao_Civil_Publica LIKE '%Sem_Sentença%' OR "
        "Acao_Civil_Publica LIKE '%Sentença_Cumprida%'"
    )

    registros = cursor.fetchall()

    if registros:
        layout = [
            [
                sg.Table(
                    values=registros,
                    headings=[
                        'ID ', '    Numero   ', 'Data_Abertura', '  Comunidade  ', '  Municipio  ', ' Area_ha ',
                        'Num_familias', 'Fase_Processo', ' Etapa_RTID ', ' Edital_DOU ', 'Edital_DOE',
                        'Portaria_DOU', 'Decreto_DOU', 'Area_ha_Titulada', '  PNRA   ', 'Relatorio_Antropologico',
                        'Latitude', 'Longitude', 'Certidao_FCP', 'Data_Certificacao', '  Sobreposicao  ',
                        'Analise_de_Sobreposicao', 'Acao_Civil_Publica', 'Data_Decisao', 'Teor_Decisao_Prazo_Sentença',
                        '          Outras_Informacoes'
                    ],
                    justification='left', 
                    auto_size_columns=True, 
                    hide_vertical_scroll=False,
                    vertical_scroll_only=False, 
                    num_rows=40
                    )
            ],

            [
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de processos: {total_acao_civil} registros encontrados com Ação Civil Pública.', font='Any 10 bold')
            ]
        ]

        janela = sg.Window('Ações Judiciais em Regularização Quilombola', layout, size=(1200, 1200), resizable=True)

        while True:
            event, _ = janela.read()

            if event == sg.WINDOW_CLOSED or event == 'Fechar':
                break

            elif event == 'Extrato':
                salvar.extrato_planilha(registros)

        janela.close()

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=constantes.FONTE)


"""Funções para exibir relatorios em janelas popups"""

def exibir_total_de_familias_em_rtids_publicados():
    conn = funcoes_registro.conectar_banco_de_dados()
    cursor = conn.cursor()
    
    cursor.execute("SELECT SUM(Num_Familias) FROM SISREQ WHERE Edital_DOU")
    total_familias = cursor.fetchone()[0]

    if total_familias is not None:
        sg.popup(f'Número de Famílias em Relatórios Publicados: {total_familias} famílias.', title='Total de Famílias', font=constantes.FONTE)
    
    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=constantes.FONTE)


def exibir_area_total_em_rtids_publicados():
    conn = funcoes_registro.conectar_banco_de_dados()
    cursor = conn.cursor()
    
    cursor.execute("SELECT SUM(Area_ha) FROM SISREQ WHERE Edital_DOU")
    total_area_rtid_publicado = cursor.fetchone()[0]

    if total_area_rtid_publicado is not None:
        total_area_formatado = "{:.2f}".format(total_area_rtid_publicado)
        sg.popup(f'Área em Relatórios Publicados: {total_area_formatado}', title='Total de Área', font=constantes.FONTE)

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=constantes.FONTE)


def exibir_area_total_em_fase_titulacao():
    conn = funcoes_registro.conectar_banco_de_dados()
    cursor = conn.cursor()
    
    cursor.execute("SELECT SUM(Area_ha) FROM SISREQ WHERE Fase_Processo LIKE '%Titulação%'")
    total_area = cursor.fetchone()[0]

    if total_area is not None:
        total_area_formatado = "{:.2f}".format(total_area)
        sg.popup(f'Área Total: {total_area_formatado} hectares em fase de Titulação.', title='Total de Área', font=constantes.FONTE)

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=constantes.FONTE)


def exibir_total_de_familias_em_fase_titulacao():
    conn = funcoes_registro.conectar_banco_de_dados()
    cursor = conn.cursor()
    
    cursor.execute("SELECT SUM(Num_Familias) FROM SISREQ WHERE Fase_Processo LIKE '%Titulação%'")
    total_familias = cursor.fetchone()[0]

    if total_familias is not None:
        sg.popup(f'Total: {total_familias} Famílias em fase de titulação.', title='Total de Famílias', font=constantes.FONTE)
    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=constantes.FONTE)


def exibir_total_de_familias_em_areas_tituladas():
    conn = funcoes_registro.conectar_banco_de_dados()
    cursor = conn.cursor()
    
    cursor.execute("SELECT SUM(Num_Familias) FROM SISREQ WHERE Area_ha_Titulada")
    total_familias = cursor.fetchone()[0]

    if total_familias is not None:
        sg.popup(f'Total: {total_familias} Famílias em áreas Tituladas.', title='Total de Famílias', font=constantes.FONTE)

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=constantes.FONTE)


def exibir_area_total_em_areas_tituladas():
    conn = funcoes_registro.conectar_banco_de_dados()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(Area_ha_Titulada) FROM SISREQ WHERE Area_ha_Titulada")
    total_area = cursor.fetchone()[0]

    if total_area is not None:
        total_area_formatado = "{:.2f}".format(total_area)
        sg.popup(f'Área Total Titulada: {total_area_formatado} hectares.', title='Total de Área', font=constantes.FONTE)

    else:
        sg.popup('Não há registros com "Títulos Expedidos" para exibir.', title='Erro', font=constantes.FONTE)
        

def exibir_total_de_familias():
    conn = funcoes_registro.conectar_banco_de_dados()
    cursor = conn.cursor()
    
    cursor.execute("SELECT SUM(Num_Familias) FROM SISREQ")
    total_familias = cursor.fetchone()[0]

    if total_familias is not None:
        total_familias_formatado = "{:.0f}".format(total_familias)
        sg.popup(f'Total: {total_familias_formatado} Famílias em processos de regularização.', title='Total de Famílias', font=constantes.FONTE)

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=constantes.FONTE)


def exibir_total_de_familias_em_territorios_identificados():
    conn = funcoes_registro.conectar_banco_de_dados()
    cursor = conn.cursor()
    
    cursor.execute("SELECT SUM(Num_familias) FROM SISREQ WHERE "
        "Relatorio_Antropologico LIKE '%Execução_Direta%' OR "
        "Relatorio_Antropologico LIKE '%Contrato%' OR "
        "Relatorio_Antropologico LIKE '%Doação%' OR "
        "Relatorio_Antropologico LIKE '%Acordo_Coop_Técnica%' OR "
        "Relatorio_Antropologico LIKE '%Termo_Execução_Descentralizada%'")

    total_familias = cursor.fetchone()[0]

    if total_familias is not None:
        total_familias_formatado = "{:.0f}".format(total_familias)
        sg.popup(f'Número de Famílias: {total_familias_formatado} Famílias em Territórios Identificados.', title='Total de Famílias', font=constantes.FONTE)

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=constantes.FONTE)


def exibir_area_total():
    conn = funcoes_registro.conectar_banco_de_dados()
    cursor = conn.cursor()
    
    cursor.execute("SELECT SUM(Area_ha) FROM SISREQ")
    total_area = cursor.fetchone()[0]

    if total_area is not None:
        total_area_formatado = "{:.2f}".format(total_area)
        sg.popup(f'Área Total: {total_area_formatado} hectares em processos de regularização.', title='Total de Área', font=constantes.FONTE)

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=constantes.FONTE)


def exibir_area_total_em_territorios_identificados():
    conn = funcoes_registro.conectar_banco_de_dados()
    cursor = conn.cursor()
    
    cursor.execute("SELECT SUM(Area_ha) FROM SISREQ WHERE "
        "Relatorio_Antropologico LIKE '%Execução_Direta%' OR "
        "Relatorio_Antropologico LIKE '%Contrato%' OR "
        "Relatorio_Antropologico LIKE '%Doação%' OR "
        "Relatorio_Antropologico LIKE '%Acordo_Coop_Técnica%' OR "
        "Relatorio_Antropologico LIKE '%Termo_Execução_Descentralizada%' "
        )
    
    totalArea = cursor.fetchone()[0]

    if totalArea is not None:
        total_area_formatado = "{:.2f}".format(totalArea)
        sg.popup(f'Área Total: {total_area_formatado} hectares em Territórios Identificados.', title='Total de Área', font=constantes.FONTE)

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=constantes.FONTE)