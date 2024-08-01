import PySimpleGUI as sg
import funcoes_banco_de_dados
import salvar
import constantes

def buscar_comunidades():
    conn = funcoes_banco_de_dados.conectar_banco_de_dados()
    cursor = conn.cursor()
    cursor.execute("SELECT Comunidade FROM SISREQ")
    return [row[0] for row in cursor.fetchall()]

comunidades = buscar_comunidades()

def atualizar_sugestoes(entrada, lista_comunidades):
    if entrada:
        return [comunidade for comunidade in lista_comunidades if comunidade.lower().startswith(entrada.lower())]
    return []

def pesquisar_por_nome_comunidade(nome_comunidade):
    conn = funcoes_banco_de_dados.conectar_banco_de_dados()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM SISREQ WHERE Comunidade = ?", (nome_comunidade,))
    registros = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) FROM SISREQ WHERE Comunidade = ?", (nome_comunidade,))
    total_comunidade = cursor.fetchone()[0]

    if registros:
        layout_resultado = [
            [
                sg.Table(registros, 
                         headings=[
                            'ID', 'Numero', 'Data_Abertura', 'Comunidade', 'Municipio', 'Area_ha',
                            'Num_familias', 'Fase_Processo', 'Etapa_RTID', 'Edital_DOU', 'Edital_DOE',
                            'Portaria_DOU', 'Decreto_DOU', 'Área_Titulada_ha', '% Área_Titulada_ha', 'Relatorio_Antropologico',
                            'Latitude', 'Longitude', 'Certidao_FCP', 'Data_Certificacao', 'Sobreposicao',
                            'Analise_de_Sobreposicao', 'Acao_Civil_Publica', 'Data_Decisao', 'Teor_Decisao_Prazo_Sentença',
                            'Outras_Informacoes'
                         ], 
                         justification='left',
                         num_rows=20,
                         key='-TABLE-',
                         auto_size_columns=True,
                         hide_vertical_scroll=False,
                         vertical_scroll_only=False)
            ],
            
            [
                sg.Button('Fechar', button_color='#ac4e04'),
                sg.Button('Extrato', button_color='green'),
                sg.Button('Alterar', button_color='#ac4e04'),
                sg.Text(f'Total de processos: {total_comunidade} registro(s) encontrado(s) para {nome_comunidade}', font='Any 10 bold')
            ]
        ]

        window2 = sg.Window('Registro por Nome de Comunidade', layout_resultado, size=(1200, 600), resizable=True)

        while True:
            event2, values2 = window2.read()
            if event2 == sg.WINDOW_CLOSED or event2 == 'Fechar':
                break
            elif event2 == 'Extrato':
                salvar.extrair_planilha(registros)
            elif event2 == 'Alterar':
                    # Função para alterar um registro do banco de dados
                    def alterarRegistroEspecifico():
                        selected_rows = window2['-TABLE-'].SelectedRows
                        if len(selected_rows) != 1:
                            sg.popup('Selecione um único registro para alterar.', title='Erro')
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

                        layoutAlterarDados = [
                            [
                                sg.Text('Numero:'), 
                                sg.Input(key='-NUMERO-', size=(20, 1), default_text=numero),
                                sg.CalendarButton('Data de Aberura', target='-DATA_ABERTURA-', key='-CALENDAR-', format='%d-%m-%Y'),
                                sg.Input(size=(15, 1), key='-DATA_ABERTURA-', default_text=data_abertura, disabled=False),
                                sg.Text('Nome da Comunidade:'), 
                                sg.Input(size=(20, 1), key='-NOME_COMUNIDADE-', default_text=nome_comunidade),
                                sg.Text('Município:'), 
                                sg.Combo(constantes.MUNICIPIOS, size=(18, 30), key='-MUNICIPIO-', default_value=municipio),
                                sg.Text('Área_ha:'), 
                                sg.Input(size=(14, 1), key='-AREA-', default_text=area_ha)
                            ],

                            [sg.Text()],

                            [
                                sg.Text('Numero de famílias:'), 
                                sg.Input(size=(15, 1), key='-NUM_FAMILIA-', default_text=num_familia),
                                sg.Text('Fase do Processo:'),
                                sg.Combo(constantes.FASE_PROCESSO, size=(18, 6), key='-FASE_PROCESSO-', default_value=fase_processo),
                                sg.Text('Etapa do RTID:'),
                                sg.Listbox(constantes.ETAPA_RTID, size=(27, 6), select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, key='-ETAPA_RTID-', default_values=etapa_rtid),
                                sg.Text('Edital DOU'), 
                                sg.Input(size=(18, 1), key='-EDITAL_DOU-', default_text=edital_dou),
                                sg.Text('Edital DOE'), 
                                sg.Input(size=(18, 1), key='-EDITAL_DOE-', default_text=edital_doe)
                            ],

                            [sg.Text()],

                            [
                                sg.CalendarButton('Portaria DOU:', target='-PORTARIA_DOU-', key='-CALENDAR-', format='%d-%m-%Y'),
                                sg.Input(key='-PORTARIA_DOU-', size=(15, 1), default_text=portaria_dou),
                                sg.CalendarButton('Decreto DOU:', target='-DECRETO_DOU-', key='-CALENDAR-', format='%d-%m-%Y'),
                                sg.Input(key='-DECRETO_DOU-', size=(15, 1), default_text=decreto_dou), 
                                sg.Text(),
                                sg.Text('Área Título_ha:'), 
                                sg.Input(size=(15, 1), key='-TITULO-', default_text=titulo),
                                sg.Text('% de Área Titulada:'), 
                                sg.Input(size=(15, 1), key='-PNRA-', default_text=pnra),
                                sg.Text('Relatório\nAntropológico'),
                                sg.Combo(constantes.RELATORIO_ANTROPOLOGICO, size=(22, 6), key='-RA-', default_value=relatorio_antropologico)
                            ],
                                
                            [sg.Text()],

                            [
                                sg.Text('Coordenadas'), 
                                sg.Text('Latitude:'), 
                                sg.Input(size=(14, 1), key='-LATITUDE-', default_text=latitude),
                                sg.Text('Longitude:'), 
                                sg.Input(size=(15, 1), key='-LONGITUDE-', default_text=longitude)
                            ],

                            [
                                sg.Text('Certidão FCP:'), 
                                sg.Combo(constantes.CERTIFICACAO_FCP, key='-CERTIDAO-', default_value=certidao_fcp),
                                sg.CalendarButton('Data Certificação:', target='-DATA_CERTIFICACAO-', key='-CALENDAR-', format='%d-%m-%Y'),
                                sg.Input(key='-DATA_CERTIFICACAO-', size=(15, 1), default_text=data_certificacao), 
                                sg.Text(), 
                                sg.Text(),
                                sg.Text(),
                                sg.Text('Sobreposição:'),
                                sg.Listbox(constantes.TIPO_SOBREPOSICAO, size=(27, 6), select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, key='-TIPO_SOBREPOSICAO-', default_values=tipo_sobreposicao),
                                sg.Text('Análise de\nSobreposição:'),
                                sg.Multiline(size=(32, 6), key='-SOBREPOSICAO-', default_text=analise_sobreposicao)
                            ],

                            [sg.Text()],

                            [
                                sg.Text('Ação Civil Pública:'), 
                                sg.Combo(constantes.ACAO_CIVIL_PUBLICA, size=(19, 1), key='-ACP-', default_value=acp),
                                sg.Text('Data Sentença\nDecisão:'),
                                sg.CalendarButton('Selecionar Data', target='-DATA_DECISAO-', key='-CALENDAR-', format='%d-%m-%Y'),
                                sg.Input(key='-DATA_DECISAO-', size=(15, 1), default_text=data_decisao),
                                sg.Text('Teor e Prazo\nda Sentença:'),
                                sg.Multiline(size=(32, 6), key='-TEOR_DECISAO-', default_text=teor_decisao),
                                sg.Text('Outras \ninformações: '),
                                sg.Multiline(size=(32, 6), key='-INFORMACAO-', default_text=outras_informacaoes)
                            ],

                            [sg.Text()],

                            [sg.Button('Salvar Alterações', button_color='#ac4e04')],

                        ]

                        janelaAlterarDados = sg.Window('Alterar ou Consultar Registro', layoutAlterarDados, size=(1250, 650), resizable=True)

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

                                sg.popup('Registro alterado com sucesso!', title='Sucesso')
                                janelaAlterarDados.close()
                                

                                # Função para consultar todos os registros do banco de dados
                                def atualizarRegistros():
                                    cursor.execute("SELECT * FROM SISREQ WHERE Comunidade = ?", (nome_comunidade,))
                                    registros = cursor.fetchall()
                                    if registros:

                                        window2['-TABLE-'].update(registros)
                                    else:
                                        sg.popup('Não há registros cadastrados.', title='Registros')
                                
                                atualizarRegistros()
                                
                                #funcoes_banco_de_dados.consultar_registros(janela)

                    alterarRegistroEspecifico()
                    
    else:
        sg.popup('Não foram encontrados registros para o nome da comunidade informado.', title='Registros')
        return