import PySimpleGUI as sg
import sqlite3
import constantes

def conectar_banco_de_dados():
    try:
        conn = sqlite3.connect('sisreq.db')
        return conn
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}", font=constantes.FONTE)
        return None

def criar_tabela_se_nao_existir(conn):
    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS SISREQ (
            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            Numero TEXT,
            Data_Abertura DATE,
            Comunidade TEXT,
            Municipio TEXT,
            Area_ha NUMERIC,
            Num_familias NUMERIC,
            Fase_Processo TEXT,
            Etapa_RTID TEXT,
            Edital_DOU TEXT,
            Edital_DOE TEXT,
            Portaria_DOU DATE,
            Decreto_DOU DATE,
            Area_ha_Titulada NUMERIC,
            Porcentagem_Titulada NUMERIC,
            Relatorio_Antropologico TEXT,
            Latitude NUMERIC,
            Longitude NUMERIC,
            Certidao_FCP TEXT,
            Data_Certificacao DATE,
            Sobreposicao TEXT,
            Analise_de_Sobreposicao TEXT,
            Acao_Civil_Publica TEXT,
            Data_Decisao DATE,
            Teor_Decisao_Prazo_Sentença TEXT,
            Outras_Informacoes TEXT
        )
        '''
    )
    conn.commit()

def inserir_dados(values, janela):
    numero = values['-NUMERO-']
    data_abertura = values['-DATA_ABERTURA-']
    nome_comunidade = values['-NOME_COMUNIDADE-']
    municipio = values['-MUNICIPIO-']
    area_ha = values['-AREA-']
    num_familia = values['-NUM_FAMILIA-']
    fase_processo = str(values['-FASE_PROCESSO-'])
    etapa_rtid = str(values['-ETAPA_RTID-'])
    edital_dou = values['-EDITAL_DOU-']
    edital_doe = values['-EDITAL_DOE-']
    portaria_dou = values['-PORTARIA_DOU-']
    decreto_dou = values['-DECRETO_DOU-']
    titulo = values['-TITULO-']
    pnra = values['-PNRA-']
    relatorio_antropologico = str(values['-RA-'])
    latitude = values['-LATITUDE-']
    longitude = values['-LONGITUDE-']
    certidao_fcp = values['-CERTIDAO-']
    data_certificacao = values['-DATA_CERTIFICACAO-']
    tipo_sobreposicao = str(values['-TIPO_SOBREPOSICAO-'])
    analise_sobreposicao = values['-SOBREPOSICAO-']
    acp = values['-ACP-']
    data_decisao = values['-DATA_DECISAO-']
    teor_decisao = values['-TEOR_DECISAO-']
    outras_informacoes = values['-INFORMACAO-']

    conn = conectar_banco_de_dados()

    if conn is not None:
        cursor = conn.cursor()
        cursor.execute("""
                INSERT INTO REGISTROS (
                        'Numero',
                        'Data_Abertura',
                        'Comunidade',
                        'Municipio',
                        'Area_ha',
                        'Num_familias',
                        'Fase_Processo',
                        'Etapa_RTID',
                        'Edital_DOU',
                        'Edital_DOE',
                        'Portaria_DOU',
                        'Decreto_DOU',
                        'Area_ha_Titulada',
                        'Porcentagem_Titulada',
                        'Relatorio_Antropologico',
                        'Latitude',
                        'Longitude',
                        'Certidao_FCP',
                        'Data_Certificacao',
                        'Sobreposicao',
                        'Analise_de_Sobreposicao',
                        'Acao_Civil_Publica',
                        'Data_Decisao',
                        'Teor_Decisao_Prazo_Sentença',
                        'Outras_Informacoes')
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                       """,
                       (
                           numero, 
                           data_abertura, 
                           nome_comunidade, 
                           municipio, 
                           area_ha, 
                           num_familia, 
                           fase_processo, 
                           etapa_rtid, 
                           edital_dou,
                           edital_doe, 
                           portaria_dou, 
                           decreto_dou, 
                           titulo, 
                           pnra, 
                           relatorio_antropologico, 
                           latitude, 
                           longitude, 
                           certidao_fcp,
                           data_certificacao, 
                           tipo_sobreposicao, 
                           analise_sobreposicao, 
                           acp, 
                           data_decisao, 
                           teor_decisao,
                           outras_informacoes
                       )
        )

        conn.commit()
        sg.popup('Dados inseridos com sucesso!', title='Sucesso', font=constantes.FONTE)

        janela['-NUMERO-'].update('')
        janela['-DATA_ABERTURA-'].update('')
        janela['-NOME_COMUNIDADE-'].update('')
        janela['-MUNICIPIO-'].update('')
        janela['-AREA-'].update('')
        janela['-NUM_FAMILIA-'].update('')
        janela['-FASE_PROCESSO-'].update('')
        janela['-ETAPA_RTID-'].update(constantes.ETAPA_RTID)
        janela['-EDITAL_DOU-'].update('')
        janela['-EDITAL_DOE-'].update('')
        janela['-PORTARIA_DOU-'].update('')
        janela['-DECRETO_DOU-'].update('')
        janela['-TITULO-'].update('')
        janela['-PNRA-'].update('')
        janela['-RA-'].update('')
        janela['-LATITUDE-'].update('')
        janela['-LONGITUDE-'].update('')
        janela['-CERTIDAO-'].update('')
        janela['-DATA_CERTIFICACAO-'].update('')
        janela['-TIPO_SOBREPOSICAO-'].update(constantes.TIPO_SOBREPOSICAO)
        janela['-SOBREPOSICAO-'].update('')
        janela['-ACP-'].update('')
        janela['-DATA_DECISAO-'].update('')
        janela['-TEOR_DECISAO-'].update('')
        janela['-INFORMACAO-'].update('')

        cursor.close()
        conn.close()

def consultar_registros(janela):
    conn = conectar_banco_de_dados()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM SISREQ")
        registros = cursor.fetchall()
        
        if registros:
            janela['-TABLE-'].update(registros)
        else:
            sg.popup('Não há registros cadastrados.', title='Registros', font=constantes.FONTE)

        cursor.close()
        conn.close()

def alterar_registro(janela):
    conn = conectar_banco_de_dados()
    if conn is not None:
        cursor = conn.cursor()

    selected_rows = janela['-TABLE-'].SelectedRows
    if len(selected_rows) != 1:
        sg.popup('Selecione um único registro para alterar.', title='Erro', font=constantes.FONTE)
        return

    selected_row_values = janela['-TABLE-'].get()[selected_rows[0]]
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

    coluna_1 = [
        [sg.Text('Número do\nProcesso:'), sg.Input(key='-NUMERO-', size=(21, 1), default_text=numero)],
        [sg.CalendarButton('Data Abertura', target='-DATA_ABERTURA-', key='-CALENDAR-', format='%d-%m-%Y'), sg.Input(size=(15, 1), key='-DATA_ABERTURA-', default_text=data_abertura, disabled=False)],
        [sg.Text('Comunidade:'), sg.Input(key='-NOME_COMUNIDADE-', size=(19, 1), default_text=nome_comunidade)],
        [sg.Text('Município:'), sg.Combo(constantes.MUNICIPIOS, size=(19, 30), key='-MUNICIPIO-', default_value=municipio)],
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
        [sg.Text('% Área\nTitulada_ha:'), sg.Input(size=(13, 1), key='-PNRA-', default_text=pnra)],
        [sg.Text('Latitude:  '), sg.Input(size=(15, 1), key='-LATITUDE-', default_text=latitude)],
        [sg.Text('Longitude:'), sg.Input(size=(15, 1), key='-LONGITUDE-', default_text=longitude)]

    ]

    coluna_4 = [
        [sg.Text('Edital DOU'), sg.Input(size=(18, 1), key='-EDITAL_DOU-', default_text=edital_dou)],
        [sg.Text('Edital DOE'), sg.Input(size=(18, 1), key='-EDITAL_DOE-', default_text=edital_doe)],
        [sg.CalendarButton('Portaria DOU:', target='-PORTARIA_DOU-', key='-CALENDAR-', format='%d-%m-%Y'), sg.Input(key='-PORTARIA_DOU-', size=(15, 1), default_text=portaria_dou)],
        [sg.CalendarButton('Decreto DOU:', target='-DECRETO_DOU-', key='-CALENDAR-', format='%d-%m-%Y'), sg.Input(key='-DECRETO_DOU-', size=(15, 1), default_text=decreto_dou)],
        [sg.Text('Sobreposição:'), sg.Listbox(constantes.TIPO_SOBREPOSICAO, size=(27, 6), select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, key='-TIPO_SOBREPOSICAO-', default_values=tipo_sobreposicao)]
    ]

    coluna_5 = [
        [sg.Text('Detalhes de\nSobreposição:'), sg.Multiline(size=(32, 6), key='-SOBREPOSICAO-', default_text=analise_sobreposicao)],
        [sg.Text('Ação Civil Pública:'), sg.Combo(constantes.ACAO_CIVIL_PUBLICA, size=(19, 1), key='-ACP-', default_value=acp)],
        [sg.CalendarButton('Data Sentença', target='-DATA_DECISAO-', key='-CALENDAR-', format='%d-%m-%Y'), sg.Input(key='-DATA_DECISAO-', size=(15, 1), default_text=data_decisao),],
        [sg.Text('Teor e Prazo \nda Sentença:'), sg.Multiline(size=(32, 6), key='-TEOR_DECISAO-', default_text=teor_decisao)],
        [sg.Text('Outras \ninformações: '), sg.Multiline(size=(32, 6), key='-INFORMACAO-', default_text=outras_informacaoes)]
    ]



    layoutAlterarDados = [
        [
            sg.Column(coluna_1), sg.VerticalSeparator(), 
            sg.Column(coluna_2), sg.VerticalSeparator(), 
            sg.Column(coluna_3), sg.VerticalSeparator(),
            sg.Column(coluna_4), sg.VerticalSeparator(), 
            sg.Column(coluna_5)
        ],

        [sg.Button('Salvar Alterações', button_color='#ac4e04')],

    ]

    janelaAlterarDados = sg.Window('Alterar Registro', layoutAlterarDados, size=(1250, 650), resizable=True)

    while True:
        event_alterar, values_alterar = janelaAlterarDados.read()

        if event_alterar == sg.WINDOW_CLOSED:
            break
        elif event_alterar == 'Salvar Alterações':
            new_numero = values_alterar['-NUMERO-']
            new_data_abertura = values_alterar['-DATA_ABERTURA-']
            new_nome_comunidade = values_alterar['-NOME_COMUNIDADE-']
            new_municipio = values_alterar['-MUNICIPIO-']
            new_area_ha = values_alterar['-AREA-']
            new_num_familia = values_alterar['-NUM_FAMILIA-']
            new_fase_processo = str(values_alterar['-FASE_PROCESSO-'])
            new_etapa_rtid = str(values_alterar['-ETAPA_RTID-'])
            new_edital_dou = values_alterar['-EDITAL_DOU-']
            new_edital_doe = values_alterar['-EDITAL_DOE-']
            new_portaria_dou = values_alterar['-PORTARIA_DOU-']
            new_decreto_dou = values_alterar['-DECRETO_DOU-']
            new_titulo = values_alterar['-TITULO-']
            new_pnra = values_alterar['-PNRA-']
            new_relatorio_antropologico = str(values_alterar['-RA-'])
            new_latitude = values_alterar['-LATITUDE-']
            new_longitude = values_alterar['-LONGITUDE-']
            new_certidao_fcp = values_alterar['-CERTIDAO-']
            new_data_certificacao = values_alterar['-DATA_CERTIFICACAO-']
            new_tipo_sobreposicao = str(values_alterar['-TIPO_SOBREPOSICAO-'])
            new_analise_sobreposicao = values_alterar['-SOBREPOSICAO-']
            new_acp = values_alterar['-ACP-']
            new_data_decisao = values_alterar['-DATA_DECISAO-']
            new_teor_decisao = values_alterar['-TEOR_DECISAO-']
            new_outras_informacoes = values_alterar['-INFORMACAO-']

            cursor.execute(
                """ 
                UPDATE SISREQ SET 
                Numero=?, 
                Data_Abertura=?, 
                Comunidade=?, 
                Municipio=?, 
                Area_ha=?, 
                Num_familias=?, 
                Fase_Processo=?, 
                Etapa_RTID=?, 
                Edital_DOU=?, 
                Edital_DOE=?, 
                Portaria_DOU=?, 
                Decreto_DOU=?, 
                Titulo=?,
                PNRA=?, 
                Relatorio_Antropologico=?, 
                Latitude=?, 
                Longitude=?, 
                Certidao_FCP=?, 
                Data_Certificacao=?, 
                Sobreposicao=?, 
                Analise_de_Sobreposicao=?, 
                Acao_Civil_Publica=?, 
                Data_Decisao=?, 
                Teor_Decisao_Prazo_Sentença=?, 
                Outras_Informacoes=?
                WHERE ID=?
            """, 

            (
                new_numero, 
                new_data_abertura, 
                new_nome_comunidade, 
                new_municipio, 
                new_area_ha, 
                new_num_familia,
                new_fase_processo, 
                new_etapa_rtid, 
                new_edital_dou, 
                new_edital_doe, 
                new_portaria_dou, 
                new_decreto_dou,
                new_titulo,
                new_pnra, 
                new_relatorio_antropologico, 
                new_latitude, 
                new_longitude, 
                new_certidao_fcp,
                new_data_certificacao,
                new_tipo_sobreposicao, 
                new_analise_sobreposicao, 
                new_acp, 
                new_data_decisao, 
                new_teor_decisao,
                new_outras_informacoes,
                selected_row_values[0]
                )
            )
            
            conn.commit()

            sg.popup('Registro alterado com sucesso!', title='Sucesso', font=constantes.FONTE)
            janelaAlterarDados.close()
            consultar_registros(janela)
            cursor.execute("SELECT COUNT(*) as Total FROM SISREQ WHERE Numero")
            totalProcesso = cursor.fetchone()[0]
            janela['total_processo'].update(f'{totalProcesso} Processos')