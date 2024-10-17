import PySimpleGUI as sg
from constantes import FONTE, headings
from funcoes_registro import conectar_banco_de_dados
from salvar import salvar_extrato_planilha

"""Funções para exibir relatórios em tabelas"""

def rtids_publicados():
    conn = conectar_banco_de_dados()
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
                sg.Text(f'Total de RTID´s Publicados: {totalRtidPublicado}', font='Any 10 bold'),
                sg.Button('Área Identificada', button_color='#ac4e04'),
                sg.Button('Número de Famílias', button_color='green')
            ]

        ]

        janela = sg.Window('Relatórios Publicados', layout, size=(1200, 700), resizable=True)

        while True:
            event, _ = janela.read()

            if event == sg.WINDOW_CLOSED or event == 'Fechar':
                break

            elif event == 'Extrato':
                salvar_extrato_planilha(registros)

            elif event == 'Número de Famílias':
                exibir_total_de_familias_em_rtids_publicados()

            elif event == 'Área Identificada':
                exibir_area_total_em_rtids_publicados()

        janela.close()

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=FONTE)


def titulos_expedidos():
    conn = conectar_banco_de_dados()
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
                sg.Text(f'Total de processos: {total_titulos_expedidos}', font='Any 10 bold'),
                sg.Button('Área Total', button_color='#ac4e04'),
                sg.Button('Número de Famílias', button_color='green')
            ]

        ]

        janela = sg.Window('Títulos Expedidos', layout, size=(1200, 700), resizable=True)

        while True:
            event, _ = janela.read()

            if event == sg.WINDOW_CLOSED or event == 'Fechar':
                break

            elif event == 'Extrato':
                salvar_extrato_planilha(registros)

            elif event == 'Área Total':
                exibir_area_total_em_areas_tituladas()

            elif event == 'Número de Famílias':
                exibir_total_de_familias_em_areas_tituladas()

        janela.close()

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=FONTE)


def territorios_identificados():
    conn = conectar_banco_de_dados()
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
                sg.Text(f'Total de Processos: {total_de_territorios_identificados} registros encontrados com Território Identificado', font='Any 10 bold'),
                sg.Button('Área Identificada', button_color='#ac4e04'),
                sg.Button('Número de Famílias', button_color='green'),
            ]
        ]

        janela = sg.Window('Territórios Identificados', layout, size=(1200, 700), resizable=True)

        while True:
            event, _ = janela.read()

            if event == sg.WINDOW_CLOSED or event == 'Fechar':
                break

            elif event == 'Extrato':
                salvar_extrato_planilha(registros)

            elif event == 'Número de Famílias':
                exibir_total_de_familias_em_territorios_identificados()

            elif event == 'Área Identificada':
                exibir_area_total_em_territorios_identificados()

        janela.close()

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=FONTE)


def territorios_nao_identificados():
    conn = conectar_banco_de_dados()
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
                        headings=headings,
                        justification='left', 
                        auto_size_columns=True, 
                        hide_vertical_scroll=False,
                        vertical_scroll_only=False, 
                        num_rows=35
                    )
            ],

            [
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de Processos: {total_de_territorios_nao_identificados} Território(s) Não Identificado(s)', font='Any 10 bold'),
            ]

        ]

        janela = sg.Window('Territórios Não-Identificados', layout, size=(1200, 700), resizable=True)

        while True:
            event, _ = janela.read()

            if event == sg.WINDOW_CLOSED or event == 'Fechar':
                break

            elif event == 'Extrato':
                salvar_extrato_planilha(registros)

        janela.close()

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=FONTE)


def exibir_comunidades_sem_certificacao():
    conn = conectar_banco_de_dados()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT (*) FROM SISREQ WHERE Certidao_FCP LIKE '%Não-certificada%'")
    total_nao_certificadas = cursor.fetchone()[0]

    cursor.execute("SELECT * FROM SISREQ WHERE Certidao_FCP LIKE '%Não-certificada%'")
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
                    num_rows=35
                    )
            ],

            [
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de processos: {total_nao_certificadas} registros sem Certificação da Palmares.', font='Any 10 bold')
            ]
        ]

        janela = sg.Window('Comunidades sem Certificação da Palmares no Processo', layout, size=(1200, 700), resizable=True)

        while True:
            event, _ = janela.read()

            if event == sg.WINDOW_CLOSED or event == 'Fechar':
                break
            elif event == 'Extrato':
                salvar_extrato_planilha(registros)

        janela.close()
    else:
        sg.popup('Não há registros para exibir.', title='Erro')


def exibir_territorios_quilombolas_em_assentamentos():
    conn = conectar_banco_de_dados()
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
                    headings=headings,
                    justification='left', 
                    auto_size_columns=True, 
                    hide_vertical_scroll=False,
                    vertical_scroll_only=False, 
                    num_rows=35)
            ],
            
            [sg.Button('Fechar', button_color='#ac4e04'), sg.Button('Extrato', button_color='green'), sg.Text(f'Total de processos: {total_territorio_quilombola_em_assentamento} registros encontrados de comunidades quilombolas em projetos de assentamento.', font='Any 10 bold')]
        ]

        janela = sg.Window('Territórios Quilombolas em Projetos de Assentamento', layout, size=(1200, 700), resizable=True)

        while True:
            event, _ = janela.read()

            if event == sg.WINDOW_CLOSED or event == 'Fechar':
                break

            elif event == 'Extrato':
                salvar_extrato_planilha(registros)

        janela.close()

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=FONTE)


def exibir_processos_com_acao_judicial():
    conn = conectar_banco_de_dados()
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
                    headings=headings,
                    justification='left', 
                    auto_size_columns=True, 
                    hide_vertical_scroll=False,
                    vertical_scroll_only=False, 
                    num_rows=35
                    )
            ],

            [
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Text(f'Total de processos: {total_acao_civil} registros encontrados com Ação Civil Pública.', font='Any 10 bold')
            ]
        ]

        janela = sg.Window('Ação Civil Pública em Regularização Quilombola', layout, size=(1200, 700), resizable=True)

        while True:
            event, _ = janela.read()

            if event == sg.WINDOW_CLOSED or event == 'Fechar':
                break

            elif event == 'Extrato':
                salvar_extrato_planilha(registros)

        janela.close()

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=FONTE)


def cadastro_pnra():
    conn = conectar_banco_de_dados()
    cursor = conn.cursor()
    
    cursor.execute(
        "SELECT COUNT(*) FROM SISREQ WHERE "
        "PNRA LIKE '%ANDAMENTO%'"
        )
    
    cadastro_pnra_andamento = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM SISREQ WHERE "
        "PNRA LIKE '%CONCLUIDO%'"
        )
    
    cadastro_pnra_concluido = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM SISREQ WHERE "
        "PNRA LIKE '%NAO-INICIADO%'"
        )
    
    cadastro_pnra_nao_iniciado = cursor.fetchone()[0]

    cursor.execute(
        "SELECT * FROM SISREQ WHERE "
        "PNRA LIKE '%ANDAMENTO%' OR "
        "PNRA LIKE '%CONCLUIDO%' OR "
        "PNRA LIKE '%NAO-INICIADO%'"
        )

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
                sg.Button('Extrato', button_color='green'), sg.Text(''),
                sg.Text(f'| Cadastro(s) Concluído(s): {cadastro_pnra_concluido}\n| Cadastro(s) em Andamento: {cadastro_pnra_andamento}\n| Cadastro(s) Não Iniciado(s): {cadastro_pnra_nao_iniciado}', font='Any 10 bold'), sg.Text(''),
                sg.Button('Número de Famílias', button_color='green'),
            ]
        ]

        janela = sg.Window('Comunidades Cadastrados no PNRA', layout, size=(1200, 700), resizable=True)

        while True:
            event, _ = janela.read()

            if event == sg.WINDOW_CLOSED or event == 'Fechar':
                break

            elif event == 'Extrato':
                salvar_extrato_planilha(registros)

            elif event == 'Número de Famílias':
               exibir_total_de_familias_cadastradas_pnra()

        janela.close()

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=FONTE)


"""Funções para exibir relatorios em janelas popups"""

def exibir_total_de_familias_cadastradas_pnra():
    conn = conectar_banco_de_dados()
    cursor = conn.cursor()
    
    cursor.execute("SELECT SUM(Num_familias) FROM SISREQ WHERE "
        "PNRA LIKE '%CONCLUIDO%'")

    total_familias = cursor.fetchone()[0]

    if total_familias is not None:
        total_familias_formatado = "{:.0f}".format(total_familias)
        sg.popup(f'Total: {total_familias_formatado} Famílias Cadastradas no Programa Nacional de Reforma Agrária.', title='Cadastro de Famílias - PNRA', font=FONTE)

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=FONTE)


def exibir_total_de_familias_em_rtids_publicados():
    conn = conectar_banco_de_dados()
    cursor = conn.cursor()
    
    cursor.execute("SELECT SUM(Num_Familias) FROM SISREQ WHERE Edital_DOU")
    total_familias = cursor.fetchone()[0]

    if total_familias is not None:
        sg.popup(f'Número de Famílias em Relatórios Publicados: {total_familias} famílias.', title='Total de Famílias', font=FONTE)
    
    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=FONTE)


def exibir_area_total_em_rtids_publicados():
    conn = conectar_banco_de_dados()
    cursor = conn.cursor()
    
    cursor.execute("SELECT SUM(Area_ha) FROM SISREQ WHERE Edital_DOU")
    total_area_rtid_publicado = cursor.fetchone()[0]

    if total_area_rtid_publicado is not None:
        total_area_formatado = "{:.2f}".format(total_area_rtid_publicado)
        sg.popup(f'Área em Relatórios Publicados: {total_area_formatado}', title='Total de Área', font=FONTE)

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=FONTE)


def exibir_area_total_em_fase_titulacao():
    conn = conectar_banco_de_dados()
    cursor = conn.cursor()
    
    cursor.execute("SELECT SUM(Area_ha) FROM SISREQ WHERE Fase_Processo LIKE '%Titulação%'")
    total_area = cursor.fetchone()[0]

    if total_area is not None:
        total_area_formatado = "{:.2f}".format(total_area)
        sg.popup(f'Área Total: {total_area_formatado} hectares em fase de Titulação.', title='Total de Área', font=FONTE)

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=FONTE)


def exibir_total_de_familias_em_fase_titulacao():
    conn = conectar_banco_de_dados()
    cursor = conn.cursor()
    
    cursor.execute("SELECT SUM(Num_Familias) FROM SISREQ WHERE Fase_Processo LIKE '%Titulação%'")
    total_familias = cursor.fetchone()[0]

    if total_familias is not None:
        sg.popup(f'Total: {total_familias} Famílias em fase de titulação.', title='Total de Famílias', font=FONTE)
    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=FONTE)


def exibir_total_de_familias_em_areas_tituladas():
    conn = conectar_banco_de_dados()
    cursor = conn.cursor()
    
    cursor.execute("SELECT SUM(Num_Familias) FROM SISREQ WHERE Area_ha_Titulada")
    total_familias = cursor.fetchone()[0]

    if total_familias is not None:
        sg.popup(f'Total: {total_familias} Famílias em áreas Tituladas.', title='Total de Famílias', font=FONTE)

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=FONTE)


def exibir_area_total_em_areas_tituladas():
    conn = conectar_banco_de_dados()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(Area_ha_Titulada) FROM SISREQ WHERE Area_ha_Titulada")
    total_area = cursor.fetchone()[0]

    if total_area is not None:
        total_area_formatado = "{:.2f}".format(total_area)
        sg.popup(f'Área Total Titulada: {total_area_formatado} hectares.', title='Total de Área', font=FONTE)

    else:
        sg.popup('Não há registros com "Títulos Expedidos" para exibir.', title='Erro', font=FONTE)
        

def exibir_total_de_familias():
    conn = conectar_banco_de_dados()
    cursor = conn.cursor()
    
    cursor.execute("SELECT SUM(Num_Familias) FROM SISREQ")
    total_familias = cursor.fetchone()[0]

    if total_familias is not None:
        total_familias_formatado = "{:.0f}".format(total_familias)
        sg.popup(f'Total: {total_familias_formatado} Famílias em processos de regularização.', title='Total de Famílias', font=FONTE)

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=FONTE)


def exibir_total_de_familias_em_territorios_identificados():
    conn = conectar_banco_de_dados()
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
        sg.popup(f'Número de Famílias: {total_familias_formatado} Famílias em Territórios Identificados.', title='Total de Famílias', font=FONTE)

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=FONTE)


def exibir_area_total():
    conn = conectar_banco_de_dados()
    cursor = conn.cursor()
    
    cursor.execute("SELECT SUM(Area_ha) FROM SISREQ")
    total_area = cursor.fetchone()[0]

    if total_area is not None:
        total_area_formatado = "{:.2f}".format(total_area)
        sg.popup(f'Área Total: {total_area_formatado} hectares em processos de regularização.', title='Total de Área', font=FONTE)

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=FONTE)


def exibir_area_total_em_territorios_identificados():
    conn = conectar_banco_de_dados()
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
        sg.popup(f'Área Total: {total_area_formatado} hectares em Territórios Identificados.', title='Total de Área', font=FONTE)

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=FONTE)