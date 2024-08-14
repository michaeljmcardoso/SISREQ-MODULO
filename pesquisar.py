import PySimpleGUI as sg
import funcoes_registro
import salvar
import constantes

def buscar_comunidade():
    conn = funcoes_registro.conectar_banco_de_dados()
    cursor = conn.cursor()
    cursor.execute("SELECT Comunidade FROM SISREQ")
    return [row[0] for row in cursor.fetchall()]

comunidades = buscar_comunidade()

def atualizar_sugestoes(entrada, lista_comunidades):
    if entrada:
        return [comunidade for comunidade in lista_comunidades if comunidade.lower().startswith(entrada.lower())]
    return []

def pesquisar_por_nome_comunidade(nome_comunidade):
    conn = funcoes_registro.conectar_banco_de_dados()
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

        window2 = sg.Window('Registros por Nome de Comunidade', layout_resultado, size=(1200, 600), resizable=True)

        while True:
            event2, values2 = window2.read()
            if event2 == sg.WINDOW_CLOSED or event2 == 'Fechar':
                break
            elif event2 == 'Extrato':
                salvar.extrato_planilha(registros)
            elif event2 == 'Alterar':
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

                        layoutAlterarDados = criar_layout_alterar_dados(numero, data_abertura, nome_comunidade, municipio, area_ha, num_familia, fase_processo, etapa_rtid, edital_dou, edital_doe, portaria_dou, decreto_dou, titulo, pnra, relatorio_antropologico, latitude, longitude, certidao_fcp, data_certificacao, tipo_sobreposicao, analise_sobreposicao, acp, data_decisao, teor_decisao, outras_informacaoes)
                        
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

                                sg.popup('Registro alterado com sucesso!', title='Sucesso')
                                janelaAlterarDados.close()
                                
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


def buscar_municipios():
    conn = funcoes_registro.conectar_banco_de_dados()
    cursor = conn.cursor()
    cursor.execute("SELECT Municipio FROM SISREQ")
    return [row[0] for row in cursor.fetchall()]

municipios = buscar_municipios()

def atualizar_sugestoes(entrada, lista_municipios):
    if entrada:
        return [municipio for municipio in lista_municipios if municipio.lower().startswith(entrada.lower())]
    return []

def pesquisar_por_nome_municipio(nome_municipio):
    conn = funcoes_registro.conectar_banco_de_dados()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM SISREQ WHERE Municipio = ?", (nome_municipio,))
    registros = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) FROM SISREQ WHERE Municipio = ?", (nome_municipio,))
    total_municipio = cursor.fetchone()[0]
    
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
                         num_rows=35,
                         key='-TABLE-',
                         auto_size_columns=True,
                         hide_vertical_scroll=False,
                         vertical_scroll_only=False)
            ],
            
            [
                sg.Button('Fechar', button_color='#ac4e04'), 
                sg.Button('Extrato', button_color='green'), 
                sg.Button('Alterar', button_color='#ac4e04'),
                sg.Text(f'Total de processos: {total_municipio} registro(s) encontrado(s) em {nome_municipio}', font='Any 10 bold')
            ]

                    ],
        window3 = sg.Window('Registros por Nome do Município', layout_resultado, size=(1200, 600), resizable=True)                                      

        while True:
            event3, values3 = window3.read()
            if event3 == sg.WINDOW_CLOSED or event3 == 'Fechar':
                break
            elif event3 == 'Extrato':
                salvar.extrato_planilha(registros)
            elif event3 == 'Alterar':
                def alterarRegistroEspecifico():
                    selected_rows = window3['-TABLE-'].SelectedRows
                    if len(selected_rows) != 1:
                        sg.popup('Selecione um único registro para consultar.', title='Erro')
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

                    layoutAlterarDados = criar_layout_alterar_dados(numero, data_abertura, nome_comunidade, municipio, area_ha, num_familia, fase_processo, etapa_rtid, edital_dou, edital_doe, portaria_dou, decreto_dou, titulo, pnra, relatorio_antropologico, latitude, longitude, certidao_fcp, data_certificacao, tipo_sobreposicao, analise_sobreposicao, acp, data_decisao, teor_decisao, outras_informacaoes)

                    janelaconsultarDados = sg.Window('Alterar Registro', layoutAlterarDados, size=(1250, 650), resizable=True)

                    while True:
                        event_consultar, values_consultar = janelaconsultarDados.read()

                        if event_consultar == sg.WINDOW_CLOSED:
                            break
                        elif event_consultar == 'Salvar Alterações':
                            new_numero = values_consultar['-NUMERO-']
                            new_data_abertura = values_consultar['-DATA_ABERTURA-']
                            new_nome_comunidade = values_consultar['-NOME_COMUNIDADE-']
                            new_municipio = values_consultar['-MUNICIPIO-']
                            new_area_ha = values_consultar['-AREA-']
                            new_num_familia = values_consultar['-NUM_FAMILIA-']
                            new_fase_processo = str(values_consultar['-FASE_PROCESSO-'])
                            new_etapa_rtid = str(values_consultar['-ETAPA_RTID-'])
                            new_edital_dou = values_consultar['-EDITAL_DOU-']
                            new_edital_doe = values_consultar['-EDITAL_DOE-']
                            new_portaria_dou = values_consultar['-PORTARIA_DOU-']
                            new_decreto_dou = values_consultar['-DECRETO_DOU-']
                            new_titulo = values_consultar['-TITULO-']
                            new_pnra = values_consultar['-PNRA-']
                            new_relatorio_antropologico = str(values_consultar['-RA-'])
                            new_latitude = values_consultar['-LATITUDE-']
                            new_longitude = values_consultar['-LONGITUDE-']
                            new_certidao_fcp = values_consultar['-CERTIDAO-']
                            new_data_certificacao = values_consultar['-DATA_CERTIFICACAO-']
                            new_tipo_sobreposicao = str(values_consultar['-TIPO_SOBREPOSICAO-'])
                            new_analise_sobreposicao = values_consultar['-SOBREPOSICAO-']
                            new_acp = values_consultar['-ACP-']
                            new_data_decisao = values_consultar['-DATA_DECISAO-']
                            new_teor_decisao = values_consultar['-TEOR_DECISAO-']
                            new_outras_informacoes = values_consultar['-INFORMACAO-']

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
                            janelaconsultarDados.close()
                            
                            def atualizarRegistros():
                                cursor.execute("SELECT * FROM SISREQ WHERE Municipio = ?", (nome_municipio,))
                                registros = cursor.fetchall()

                                if registros:
                                    window3['-TABLE-'].update(registros)
                                else:
                                    sg.popup('Não há registros cadastrados.', title='Registros')
                            
                            atualizarRegistros()
                            #aplicacao.Aplicacao.consultar_registros()
                
                alterarRegistroEspecifico()

    else:
        sg.popup('Não foram encontrados registros para o nome do município informado.', title='Registros')
        return

def buscar_processo():
    conn = funcoes_registro.conectar_banco_de_dados()
    cursor = conn.cursor()
    cursor.execute("SELECT Numero FROM SISREQ")
    return [row[0] for row in cursor.fetchall()]

processos = buscar_processo()

def atualizar_sugestoes(entrada, lista_processos):
    if entrada:
        return [processo for processo in lista_processos if processo.lower().startswith(entrada.lower())]
    return []

def pesquisar_por_num_processo(num_processo):
    conn = funcoes_registro.conectar_banco_de_dados()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM SISREQ WHERE Numero = ?", (num_processo,))
    registros = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) FROM SISREQ WHERE Numero = ?", (num_processo,))
    total_processo = cursor.fetchone()[0]

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
                sg.Text(f'Total de processos: {total_processo} registro(s) encontrado(s) para {num_processo}', font='Any 10 bold')
            ]
        ]

        window4 = sg.Window('Registros por Número do Processo', layout_resultado, size=(1200, 600), resizable=True)

        while True:
            event4, values4 = window4.read()
            if event4 == sg.WINDOW_CLOSED or event4 == 'Fechar':
                break
            elif event4 == 'Extrato':
                salvar.extrato_planilha(registros)
            elif event4 == 'Alterar':
                    def alterarRegistroEspecifico():
                        selected_rows = window4['-TABLE-'].SelectedRows
                        if len(selected_rows) != 1:
                            sg.popup('Selecione um único registro para alterar.', title='Erro')
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

                        layoutAlterarDados = criar_layout_alterar_dados(numero, data_abertura, nome_comunidade, municipio, area_ha, num_familia, fase_processo, etapa_rtid, edital_dou, edital_doe, portaria_dou, decreto_dou, titulo, pnra, relatorio_antropologico, latitude, longitude, certidao_fcp, data_certificacao, tipo_sobreposicao, analise_sobreposicao, acp, data_decisao, teor_decisao, outras_informacaoes)
                        
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

                                sg.popup('Registro alterado com sucesso!', title='Sucesso')
                                janelaAlterarDados.close()
                                
                                def atualizarRegistros():
                                    cursor.execute("SELECT * FROM SISREQ WHERE Numero = ?", (num_processo,))
                                    registros = cursor.fetchall()
                                    if registros:

                                        window4['-TABLE-'].update(registros)
                                    else:
                                        sg.popup('Não há registros cadastrados.', title='Registros')
                                
                                atualizarRegistros()
                                #funcoes_banco_de_dados.consultar_registros(janela)

                    alterarRegistroEspecifico()
                    
    else:
        sg.popup('Não foram encontrados registros para o número do processo informado.', title='Registros')
        return


def criar_layout_alterar_dados(numero, data_abertura, nome_comunidade, municipio, area_ha, num_familia, fase_processo, etapa_rtid, edital_dou, edital_doe, portaria_dou, decreto_dou, titulo, pnra, relatorio_antropologico, latitude, longitude, certidao_fcp, data_certificacao, tipo_sobreposicao, analise_sobreposicao, acp, data_decisao, teor_decisao, outras_informacaoes):
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

    return layoutAlterarDados