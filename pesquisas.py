import PySimpleGUI as sg
import constantes
import sqlite3
from salvar import salvar_extrato_planilha 
from funcoes import conectar_banco_de_dados, criar_tabela_se_nao_existir

"""Funções de busca por nome da comunidade, município e número do processo"""

def buscar_comunidade():
    conn = conectar_banco_de_dados()
    cursor = conn.cursor()

    criar_tabela_se_nao_existir(conn)

    cursor.execute("SELECT Comunidade FROM SISREQ")
    return [row[0] for row in cursor.fetchall()]

comunidades = buscar_comunidade()


def atualizar_sugestoes(entrada, lista_comunidades):
    if entrada:
        return [comunidade for comunidade in lista_comunidades if comunidade.lower().startswith(entrada.lower())]
    return []


def pesquisar_por_nome_comunidade(nome_comunidade):
    conn = conectar_banco_de_dados()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM SISREQ WHERE Comunidade = ?", (nome_comunidade,))
    registros = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) FROM  SISREQ WHERE Comunidade = ?", (nome_comunidade,))
    total_comunidade = cursor.fetchone()[0]

    if registros:
        layout_resultado = [
            [
                sg.Table(registros, 
                         headings=constantes.headings, 
                         justification='left',
                         num_rows=20,
                         key='-TABLE-',
                         auto_size_columns=True,
                         hide_vertical_scroll=False,
                         vertical_scroll_only=False)
            ],
            
            [
                sg.Button('Extrato', button_color='green'),
                sg.Button('Consultar', button_color='#ac4e04'),
                sg.Text(f'Total de processos: {total_comunidade} registro(s) encontrado(s) para {nome_comunidade}', font='Any 10 bold')
            ]
        ]

        window2 = sg.Window('REGISTROS POR NOME DE COMUNIDADE', layout_resultado, size=(1200, 600), resizable=True)

        while True:
            event2, values2 = window2.read()
            if event2 == sg.WINDOW_CLOSED:
                break

            elif event2 == 'Extrato':
                salvar_extrato_planilha(registros)

            elif event2 == 'Consultar':
                    def consultarRegistroEspecifico():
                        selected_rows = window2['-TABLE-'].SelectedRows
                        if len(selected_rows) != 1:
                            sg.popup('Selecione um único registro para consultar.', title='Erro', font=constantes.FONTE)
                            return

                        selected_row_values = window2['-TABLE-'].get()[selected_rows[0]]
                        numero = selected_row_values[1]
                        data_abertura = selected_row_values[2]
                        nome_comunidade = selected_row_values[3]
                        municipio = selected_row_values[4]
                        area_ha = selected_row_values[5]
                        num_familia = selected_row_values[6]
                        fase_processo = selected_row_values[7]
                        etapa_rtid = selected_row_values[8]
                        edital_dou = selected_row_values[9]
                        edital_doe = selected_row_values[10]
                        portaria_dou = selected_row_values[11]
                        decreto_dou = selected_row_values[12]
                        titulo = selected_row_values[13]
                        pnra = selected_row_values[14]
                        relatorio_antropologico = selected_row_values[15]
                        latitude = selected_row_values[16]
                        longitude = selected_row_values[17]
                        certidao_fcp = selected_row_values[18]
                        data_certificacao = selected_row_values[19]
                        tipo_sobreposicao = selected_row_values[20]
                        analise_sobreposicao = selected_row_values[21]
                        acp = selected_row_values[22]
                        data_decisao = selected_row_values[23]
                        teor_decisao = selected_row_values[24]
                        outras_informacaoes = selected_row_values[25]

                        layoutConsultarDados = criar_layout_consultar_dados(numero, data_abertura, nome_comunidade, municipio, area_ha, num_familia, fase_processo, etapa_rtid, edital_dou, edital_doe, portaria_dou, decreto_dou, titulo, pnra, relatorio_antropologico, latitude, longitude, certidao_fcp, data_certificacao, tipo_sobreposicao, analise_sobreposicao, acp, data_decisao, teor_decisao, outras_informacaoes)
                        
                        janelaConsultarDados = sg.Window('CONSULTAR REGISTRO', layoutConsultarDados, size=(1400, 650), resizable=True)

                        while True:
                            event_consultar, values_consultar = janelaConsultarDados.read()

                            if event_consultar == sg.WINDOW_CLOSED:
                                break
                            else:
                                None

                    consultarRegistroEspecifico()
                    
    else:
        sg.popup('Não foram encontrados registros para o nome da comunidade informado.', title='Registros', font=constantes.FONTE)
        return


def buscar_municipios():
    conn = conectar_banco_de_dados()
    cursor = conn.cursor()

    cursor.execute("SELECT Municipio FROM SISREQ")
    return [row[0] for row in cursor.fetchall()]

municipios = buscar_municipios()


def atualizar_sugestoes(entrada, lista_municipios):
    if entrada:
        return [municipio for municipio in lista_municipios if municipio.lower().startswith(entrada.lower())]
    return []


def pesquisar_por_nome_municipio(nome_municipio):
    conn = conectar_banco_de_dados()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM SISREQ WHERE Municipio = ?", (nome_municipio,))
    registros = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) FROM SISREQ WHERE Municipio = ?", (nome_municipio,))
    total_municipio = cursor.fetchone()[0]
    
    if registros:
        layout_resultado = [
            [
                sg.Table(registros, 
                         headings=constantes.headings,
                         justification='left',
                         num_rows=30,
                         key='-TABLE-',
                         auto_size_columns=True,
                         hide_vertical_scroll=False,
                         vertical_scroll_only=False)
            ],
            
            [
                sg.Button('Extrato', button_color='green'), 
                sg.Button('Consultar', button_color='#ac4e04'),
                sg.Text(f'Total de processos: {total_municipio} registro(s) encontrado(s) em {nome_municipio}', font='Any 10 bold')
            ]

                    ],
        window3 = sg.Window('REGISTROS POR NOME DO MUNICÍPIO', layout_resultado, size=(1200, 600), resizable=True)                                      

        while True:
            event3, values3 = window3.read()
            if event3 == sg.WINDOW_CLOSED:
                break

            elif event3 == 'Extrato':
                salvar_extrato_planilha(registros)

            elif event3 == 'Consultar':
                def consultarRegistroEspecifico():
                    selected_rows = window3['-TABLE-'].SelectedRows
                    if len(selected_rows) != 1:
                        sg.popup('Selecione um único registro para consultar.', title='Erro', font=constantes.FONTE)
                        return

                    selected_row_values = window3['-TABLE-'].get()[selected_rows[0]]
                    numero = selected_row_values[1]
                    data_abertura = selected_row_values[2]
                    nome_comunidade = selected_row_values[3]
                    municipio = selected_row_values[4]
                    area_ha = selected_row_values[5]
                    num_familia = selected_row_values[6]
                    fase_processo = selected_row_values[7]
                    etapa_rtid = selected_row_values[8]
                    edital_dou = selected_row_values[9]
                    edital_doe = selected_row_values[10]
                    portaria_dou = selected_row_values[11]
                    decreto_dou = selected_row_values[12]
                    titulo = selected_row_values[13]
                    pnra = selected_row_values[14]
                    relatorio_antropologico = selected_row_values[15]
                    latitude = selected_row_values[16]
                    longitude = selected_row_values[17]
                    certidao_fcp = selected_row_values[18]
                    data_certificacao = selected_row_values[19]
                    tipo_sobreposicao = selected_row_values[20]
                    analise_sobreposicao = selected_row_values[21]
                    acp = selected_row_values[22]
                    data_decisao = selected_row_values[23]
                    teor_decisao = selected_row_values[24]
                    outras_informacaoes = selected_row_values[25]

                    layoutConsultarDados = criar_layout_consultar_dados(numero, data_abertura, nome_comunidade, municipio, area_ha, num_familia, fase_processo, etapa_rtid, edital_dou, edital_doe, portaria_dou, decreto_dou, titulo, pnra, relatorio_antropologico, latitude, longitude, certidao_fcp, data_certificacao, tipo_sobreposicao, analise_sobreposicao, acp, data_decisao, teor_decisao, outras_informacaoes)

                    janelaConsultarDados = sg.Window('CONSULTAR REGISTRO', layoutConsultarDados, size=(1400, 650), resizable=True)

                    while True:
                        event_consultar, values_consultar = janelaConsultarDados.read()

                        if event_consultar == sg.WINDOW_CLOSED:
                            break
                        else:
                            None

                consultarRegistroEspecifico()

    else:
        sg.popup('Não foram encontrados registros para o nome do município informado.', title='Registros', font=constantes.FONTE)
        return
    

def buscar_processo():
    conn = conectar_banco_de_dados()
    cursor = conn.cursor()

    cursor.execute("SELECT Numero FROM SISREQ")
    return [row[0] for row in cursor.fetchall()]

processos = buscar_processo()


def atualizar_sugestoes(entrada, lista_processos):
    if entrada:
        return [processo for processo in lista_processos if processo.lower().startswith(entrada.lower())]
    return []


def pesquisar_por_num_processo(num_processo):
    conn = conectar_banco_de_dados()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM SISREQ WHERE Numero = ?", (num_processo,))
    registros = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) FROM SISREQ WHERE Numero = ?", (num_processo,))
    total_processo = cursor.fetchone()[0]

    if registros:
        layout_resultado = [
            [
                sg.Table(registros, 
                         headings=constantes.headings, 
                         justification='left',
                         num_rows=20,
                         key='-TABLE-',
                         auto_size_columns=True,
                         hide_vertical_scroll=False,
                         vertical_scroll_only=False)
            ],
            
            [
                sg.Button('Extrato', button_color='green'),
                sg.Button('Consultar', button_color='#ac4e04'),
                sg.Text(f'Total de processos: {total_processo} registro(s) encontrado(s) para {num_processo}', font='Any 10 bold')
            ]
        ]

        window4 = sg.Window('REGISTROS POR NÚMERO DO PROCESSO', layout_resultado, size=(1200, 600), resizable=True)

        while True:
            event4, values4 = window4.read()
            if event4 == sg.WINDOW_CLOSED:
                break

            elif event4 == 'Extrato':
                salvar_extrato_planilha(registros)

            elif event4 == 'Consultar':
                    def consultarRegistroEspecifico():
                        selected_rows = window4['-TABLE-'].SelectedRows
                        if len(selected_rows) != 1:
                            sg.popup('Selecione um único registro para consultar.', title='Erro', font=constantes.FONTE)
                            return

                        selected_row_values = window4['-TABLE-'].get()[selected_rows[0]]
                        numero = selected_row_values[1]
                        data_abertura = selected_row_values[2]
                        nome_comunidade = selected_row_values[3]
                        municipio = selected_row_values[4]
                        area_ha = selected_row_values[5]
                        num_familia = selected_row_values[6]
                        fase_processo = selected_row_values[7]
                        etapa_rtid = selected_row_values[8]
                        edital_dou = selected_row_values[9]
                        edital_doe = selected_row_values[10]
                        portaria_dou = selected_row_values[11]
                        decreto_dou = selected_row_values[12]
                        titulo = selected_row_values[13]
                        pnra = selected_row_values[14]
                        relatorio_antropologico = selected_row_values[15]
                        latitude = selected_row_values[16]
                        longitude = selected_row_values[17]
                        certidao_fcp = selected_row_values[18]
                        data_certificacao = selected_row_values[19]
                        tipo_sobreposicao = selected_row_values[20]
                        analise_sobreposicao = selected_row_values[21]
                        acp = selected_row_values[22]
                        data_decisao = selected_row_values[23]
                        teor_decisao = selected_row_values[24]
                        outras_informacaoes = selected_row_values[25]

                        layoutConsultarDados = criar_layout_consultar_dados(numero, data_abertura, nome_comunidade, municipio, area_ha, num_familia, fase_processo, etapa_rtid, edital_dou, edital_doe, portaria_dou, decreto_dou, titulo, pnra, relatorio_antropologico, latitude, longitude, certidao_fcp, data_certificacao, tipo_sobreposicao, analise_sobreposicao, acp, data_decisao, teor_decisao, outras_informacaoes)
                        
                        janelaConsultarDados = sg.Window('CONSULTAR REGISTRO', layoutConsultarDados, size=(1400, 650), resizable=True)

                        while True:
                            event_consultar, values_consultar = janelaConsultarDados.read()

                            if event_consultar == sg.WINDOW_CLOSED:
                                break
                            else:
                                None
                            
                    consultarRegistroEspecifico()
                    
    else:
        sg.popup('Não foram encontrados registros para o número do processo informado.', title='Registros', font=constantes.FONTE)
        return


def criar_layout_consultar_dados(numero, data_abertura, nome_comunidade, municipio, area_ha, num_familia, fase_processo, etapa_rtid, edital_dou, edital_doe, portaria_dou, decreto_dou, titulo, pnra, relatorio_antropologico, latitude, longitude, certidao_fcp, data_certificacao, tipo_sobreposicao, analise_sobreposicao, acp, data_decisao, teor_decisao, outras_informacaoes):
    coluna_1 = [
        [sg.Text('Número do\nProcesso:'), sg.Input(key='-NUMERO-', size=(21, 1), default_text=numero)],
        [sg.CalendarButton('Data Abertura', target='-DATA_ABERTURA-', key='-CALENDAR-', format='%d-%m-%Y'), sg.Input(size=(15, 1), key='-DATA_ABERTURA-', default_text=data_abertura, disabled=False)],
        [sg.Text('Comunidade:'), sg.Input(key='-NOME_COMUNIDADE-', size=(19, 1), default_text=nome_comunidade)],
        [sg.Text('Município:'), sg.Combo(constantes.MUNICIPIOS, size=(19, 30), key='-MUNICIPIO-', default_value=municipio)],
        #[sg.Text('Município:'), sg.Input(size=(19, 30), key='-MUNICIPIO-', default_text=municipio)],
        [sg.Text('Número de\nFamílias:'), sg.Input(size=(21, 1), key='-NUM_FAMILIA-', default_text=num_familia)]
    ]

    coluna_2 = [
        [sg.Text('Fase:'), sg.Combo(constantes.FASE_PROCESSO, size=(24, 6), key='-FASE_PROCESSO-', default_value=fase_processo)],
        [sg.Text('Etapa\nRTID:'), sg.Listbox(constantes.ETAPA_RTID, size=(24, 3), select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, key='-ETAPA_RTID-', default_values=etapa_rtid)],
        [sg.Text('Antropológico:'), sg.Combo(constantes.RELATORIO_ANTROPOLOGICO, size=(17, 6), key='-RA-', default_value=relatorio_antropologico)],
        [sg.Text('Certidão FCP:'), sg.Combo(constantes.CERTIFICACAO_FCP, size=(17, 6), key='-CERTIDAO-', default_value=certidao_fcp)],
        [sg.CalendarButton('Data Certificação', target='-DATA_CERTIFICACAO-', key='-CALENDAR-', format='%d-%m-%Y'), sg.Input(size=(13, 1), key='-DATA_CERTIFICACAO-', default_text=data_certificacao, disabled=False)]
    ]

    coluna_3 = [
        [sg.Text('Área\nIdentificada_ha:'), sg.Input(size=(10, 1), key='-AREA-', default_text=area_ha)],
        [sg.Text('Área\nTitulada_ha:'), sg.Input(size=(13, 1), key='-TITULO-', default_text=titulo)],
        [sg.Text('PNRA\nQuilombola:'), sg.Combo(constantes.PNRA, size=(13, 1), key='-PNRA-', default_value=pnra)],
        [sg.Text('Latitude:  '), sg.Input(size=(15, 1), key='-LATITUDE-', default_text=latitude)],
        [sg.Text('Longitude:'), sg.Input(size=(15, 1), key='-LONGITUDE-', default_text=longitude)]

    ]

    coluna_4 = [
        [sg.Text('Edital DOU'), sg.Input(size=(18, 1), key='-EDITAL_DOU-', default_text=edital_dou)],
        [sg.Text('Edital DOE'), sg.Input(size=(18, 1), key='-EDITAL_DOE-', default_text=edital_doe)],
        [sg.CalendarButton('Portaria DOU:', target='-PORTARIA_DOU-', key='-CALENDAR-', format='%d-%m-%Y'), sg.Input(key='-PORTARIA_DOU-', size=(15, 1), default_text=portaria_dou)],
        [sg.CalendarButton('Decreto DOU:', target='-DECRETO_DOU-', key='-CALENDAR-', format='%d-%m-%Y'), sg.Input(key='-DECRETO_DOU-', size=(15, 1), default_text=decreto_dou)],
        [sg.Text('Sobreposição:'), sg.Listbox(constantes.TIPO_SOBREPOSICAO, size=(20, 6), select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, key='-TIPO_SOBREPOSICAO-', default_values=tipo_sobreposicao)]
    ]

    coluna_5 = [
        [sg.Text('Detalhes de\nSobreposição:'), sg.Multiline(size=(32, 3), key='-SOBREPOSICAO-', default_text=analise_sobreposicao)],
        [sg.Text('Ação Civil Pública:'), sg.Combo(constantes.ACAO_CIVIL_PUBLICA, size=(19, 1), key='-ACP-', default_value=acp)],
        [sg.CalendarButton('Data Sentença', target='-DATA_DECISAO-', key='-CALENDAR-', format='%d-%m-%Y'), sg.Input(key='-DATA_DECISAO-', size=(15, 1), default_text=data_decisao),],
        [sg.Text('Teor e Prazo \nda Sentença:'), sg.Multiline(size=(32, 3), key='-TEOR_DECISAO-', default_text=teor_decisao)],
        [sg.Text('Outras \ninformações: '), sg.Multiline(size=(32, 3), key='-INFORMACAO-', default_text=outras_informacaoes)]
    ]

    layoutConsultarDados = [
        [
            sg.Column(coluna_1), sg.VerticalSeparator(), 
            sg.Column(coluna_2), sg.VerticalSeparator(), 
            sg.Column(coluna_3), sg.VerticalSeparator(),
            sg.Column(coluna_4), sg.VerticalSeparator(), 
            sg.Column(coluna_5)
        ],

    ]

    return layoutConsultarDados


# Função para buscar municípios de todo Brasil com base em uma string digitada
def buscar_municipios_do_brasil(nome_parcial):
    conn_municipios = sqlite3.connect('municipios.db')
    cursor_municipios = conn_municipios.cursor()
    
    # Busca por municípios que contenham a string digitada
    cursor_municipios.execute("SELECT nome FROM municipios WHERE nome LIKE ?", ('%' + nome_parcial + '%',))
    resultados = cursor_municipios.fetchall()
    
    conn_municipios.close()
    
    # Retorna apenas o nome dos municípios
    return [resultado[0] for resultado in resultados]