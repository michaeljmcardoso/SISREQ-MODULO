import PySimpleGUI as sg
import funcoes_banco_de_dados
import salvar
import filtrar
import funcoes_pesquisar
import constantes

class Aplicacao:
    def __init__(self):
        self.janela = self.criar_janela()

    def iniciar(self):
        while True:
            event, values = self.janela.read()
            if event == 'SAIR' or event == sg.WIN_CLOSED:
                break
            elif event == 'INSERIR':
                funcoes_banco_de_dados.inserir_dados(values, self.janela)
                funcoes_banco_de_dados.consultar_registros(self.janela)
            elif event == 'CONSULTAR':
                funcoes_banco_de_dados.consultar_registros(self.janela)
            elif event == 'ALTERAR':
                funcoes_banco_de_dados.alterar_registro(self.janela)
            elif event == 'Extrair Planilha':
                salvar.planilha(self.janela)
            elif event == 'Inicial':
                filtrar.fase_inicial()
            elif event == 'RTID':
                filtrar.fase_Rtid()
            elif event == 'Publicação':
                filtrar.fase_publicacao()
            elif event == 'Notificação':
                filtrar.fase_notificacao()
            elif event == 'Contestação':
                filtrar.fase_contestacao()
            elif event == 'Recurso':
                filtrar.fase_recurso()
            elif event == 'Portaria':
                filtrar.fase_portaria()
            elif event == 'Decreto':
                filtrar.fase_decreto()
            elif event == 'Titulação':
                filtrar.fase_titulacao()
            elif event == 'Desintrusão':
                filtrar.fase_desintrusao()
            elif event == 'Desapropriação':
                filtrar.fase_desapropriacao()
            elif event == 'Pesquisar':
                self.criar_janela_pesquisar()

            # Evento de digitação no campo de entrada comunidade
            elif event == '-NOME_COMUNIDADES-':
                entrada = values['-NOME_COMUNIDADES-']
                sugestoes = funcoes_pesquisar.atualizar_sugestoes(entrada, funcoes_pesquisar.comunidades)

                if sugestoes:
                    self.janela['-SUGESTOES-'].update(sugestoes, visible=True)
                else:
                    self.janela['-SUGESTOES-'].update(visible=False)

            # Evento de seleção na lista de sugestões comunidade
            if event == '-SUGESTOES-':
                selecao = values['-SUGESTOES-'][0]
                self.janela['-NOME_COMUNIDADES-'].update(selecao)
                self.janela['-SUGESTOES-'].update(visible=False)

            # Evento do botão OK ou pressionar Enter
            if event == '-OK-' or event == '\r':
                nome_comunidade = values['-NOME_COMUNIDADES-']
                if nome_comunidade:
                    funcoes_pesquisar.pesquisar_por_nome_comunidade(nome_comunidade)
                else:
                    sg.popup('Por favor, digite o nome de uma comunidade.', title='Erro')
            elif event == 'Buscar Comunidade':
                funcoes_pesquisar.pesquisar_por_nome_comunidade(self.janela)
            
             # Evento de digitação no campo de entrada municipio
            elif event == '-MUNICIPIOS-':
                entrada = values['-MUNICIPIOS-']
                sugestoes = funcoes_pesquisar.atualizar_sugestoes(entrada, funcoes_pesquisar.municipios)

                if sugestoes:
                    self.janela['-SUGESTOES-'].update(sugestoes, visible=True)
                else:
                    self.janela['-SUGESTOES-'].update(visible=False)

            # Evento de seleção na lista de sugestões municipio
            if event == '-SUGESTOES-':
                selecao = values['-SUGESTOES-'][0]
                self.janela['-MUNICIPIOS-'].update(selecao)
                self.janela['-SUGESTOES-'].update(visible=False)

            # Evento do botão OK ou pressionar Enter
            if event == '-OK-' or event == '\r':
                nome_municipio = values['-MUNICIPIOS-']
                if nome_municipio:
                    funcoes_pesquisar.pesquisar_por_nome_municipio(nome_municipio)
                else:
                    sg.popup('Por favor, digite o nome de um município.', title='Erro')
            elif event == 'Buscar Municipio':
                funcoes_pesquisar.pesquisar_por_nome_municipio(self.janela)

        self.janela.close()

    def criar_janela(self):
        sg.theme(constantes.JANELA_TEMA)

        coluna_1 = [
            [sg.Text('Número do\nProcesso:'), sg.Input(key='-NUMERO-', size=(21, 1))],
            [sg.CalendarButton('Data Abertura', target='-DATA_ABERTURA-', key='-CALENDAR-', format='%d-%m-%Y'), sg.Input(size=(15, 1), key='-DATA_ABERTURA-', disabled=False)],
            [sg.Text('Comunidade:'), sg.Input(key='-NOME_COMUNIDADE-', size=(19, 1))],
            [sg.Text('Município:'), sg.Combo(constantes.MUNICIPIOS, size=(19, 30), key='-MUNICIPIO-')],
            [sg.Text('Número de\nFamílias:'), sg.Input(size=(21, 1), key='-NUM_FAMILIA-')]
        ]

        coluna_2 = [
            [sg.Text('Fase:'), sg.Combo(constantes.FASE_PROCESSO, size=(24, 6), key='-FASE_PROCESSO-')],
            [sg.Text('Etapa\nRTID:'), sg.Listbox(constantes.ETAPA_RTID, size=(24, 3), select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, key='-ETAPA_RTID-')],
            [sg.Text('Antropológico:'), sg.Combo(constantes.RELATORIO_ANTROPOLOGICO, size=(17, 6), key='-RA-')],
            [sg.Text('Certidão FCP:'), sg.Combo(constantes.CERTIFICACAO_FCP, size=(17, 6), key='-CERTIDAO-')],
            [sg.CalendarButton('Data Certificação', target='-DATA_CERTIFICACAO-', key='-CALENDAR-', format='%d-%m-%Y'), sg.Input(size=(13, 1), key='-DATA_CERTIFICACAO-', disabled=False)]
        ]

        coluna_3 = [
            [sg.Text('Área\nIdentificada_ha:'), sg.Input(size=(10, 1), key='-AREA-')],
            [sg.Text('Área\nTitulada_ha:'), sg.Input(size=(13, 1), key='-TITULO-')],
            [sg.Text('% Área\nTitulada_ha:'), sg.Input(size=(13, 1), key='-PNRA-')],
            [sg.Text('Latitude:  '), sg.Input(size=(15, 1), key='-LATITUDE-')],
            [sg.Text('Longitude:'), sg.Input(size=(15, 1), key='-LONGITUDE-')]
        ]

        coluna_4 = [
            [sg.Text('Edital DOU:'), sg.Input(size=(20, 1), key='-EDITAL_DOU-')],
            [sg.Text('Edital DOE:'), sg.Input(size=(20, 1), key='-EDITAL_DOE-')],
            [sg.CalendarButton('Portaria DOU', target='-PORTARIA_DOU-', key='-CALENDAR-', format='%d-%m-%Y'), sg.Input(size=(15, 1), key='-PORTARIA_DOU-', disabled=False)],
            [sg.CalendarButton('Decreto DOU', target='-DECRETO_DOU-', key='-CALENDAR-', format='%d-%m-%Y'), sg.Input(size=(15, 1), key='-DECRETO_DOU-', disabled=False)],
            [sg.Text('Sobreposição\nTerritorial:'), sg.Listbox(constantes.TIPO_SOBREPOSICAO, size=(22, 3), select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, key='-TIPO_SOBREPOSICAO-')]
        ]

        coluna_5 = [
            [sg.Text('Detalhes de\nSobreposição:'), sg.Multiline(size=(24, 2), key='-SOBREPOSICAO-')],
            [sg.Text('Ação Civil Pública:'), sg.Combo(constantes.ACAO_CIVIL_PUBLICA, size=(20, 1), key='-ACP-')],
            [sg.CalendarButton('Data Sentença', target='-DATA_DECISAO-', key='-CALENDAR-', format='%d-%m-%Y'), sg.Input(size=(22, 1), key='-DATA_DECISAO-', disabled=False)],
            [sg.Text('Teor_Prazo da  \nSentença:'), sg.Multiline(size=(22, 2), key='-TEOR_DECISAO-')],
            [sg.Text('Outras Informações:'), sg.Multiline(size=(18, 2), key='-INFORMACAO-')]
        ]

        coluna_botoes = [
            [sg.Button('INSERIR', button_color='#ac4e04'), sg.Button('CONSULTAR', button_color='#ac4e04'), sg.Button('ALTERAR', button_color='#ac4e04')]
        ]

        layout = [
            [sg.Column(coluna_1), sg.VerticalSeparator(),
             sg.Column(coluna_2), sg.VerticalSeparator(),
             sg.Column(coluna_3), sg.VerticalSeparator(),
             sg.Column(coluna_4), sg.VerticalSeparator(),
             sg.Column(coluna_5)
            ],

            [sg.Column(coluna_botoes), sg.VerticalSeparator(), sg.Button('Pesquisar', button_color='#3169F5')],

            [sg.Button('Inicial', button_color='green'), sg.Button('RTID', button_color='green'), sg.Button('Publicação', button_color='green'), sg.Button('Notificação', button_color='green'), sg.Button('Contestação', button_color='green'), sg.Button('Recurso', button_color='green'), sg.Button('Portaria', button_color='green'), sg.Button('Decreto', button_color='green'), sg.Button('Desapropriação', button_color='green'), sg.Button('Titulação', button_color='green'), sg.Button('Desintrusão', button_color='green')],

            [sg.Table(
                values=[],
                headings=[
                    'ID ', '    Numero   ', 'Data_Abertura', '  Comunidade  ', '  Municipio  ', ' Area_ha ',
                    'Num_familias', 'Fase_Processo', ' Etapa_RTID ', ' Edital_DOU ', 'Edital_DOE',
                    'Portaria_DOU', 'Decreto_DOU', 'Area_ha_Titulada', 'Porcentagem_Titulada', 'Relatorio_Antropologico',
                    'Latitude', 'Longitude', 'Certidao_FCP', 'Data_Certificacao', '  Sobreposicao  ',
                    'Analise_de_Sobreposicao', 'Acao_Civil_Publica', 'Data_Decisao', 'Teor_Decisao_Prazo_Sentença',
                    '          Outras_Informacoes'
                ],
                num_rows=20,
                key='-TABLE-',
                hide_vertical_scroll=False,
                vertical_scroll_only=False,
                justification='left',
                auto_size_columns=True,
            )],

            [sg.Button('Extrair Planilha', button_color='green')],

            [sg.Text('', size=(75, 1)), constantes.JANELA_RODAPE, sg.Text('', size=(0, 1))]
        ]

        janela = sg.Window("SISREQ - Sistema de Regularização Quilombola (v.1.1.0)", layout, resizable=True)
        return janela

    def criar_janela_pesquisar(self):
        coluna_pesquisar = [
            [sg.Text('Pesquisar Comunidade:'), sg.Input(size=(25, 1), key='-NOME_COMUNIDADES-', enable_events=True), sg.Listbox(values=[], size=(25, 4), key='-SUGESTOES-', enable_events=True, visible=False), sg.Button('OK', key='-OK-')],
            [sg.Text('Pesquisar Município:    '), sg.Input(size=(25, 1), key='-MUNICIPIOS-', enable_events=True), sg.Listbox(values=[], size=(25, 4), key='-SUGESTOES1-', enable_events=True, visible=False), sg.Button('OK', key='-OK1-')],
            [sg.Text('Pesquisar Processo:    '), sg.Input(size=(25, 1), key='-NUP-', enable_events=True), sg.Listbox(values=[], size=(25, 4), key='-SUGESTOES-', enable_events=True, visible=False), sg.Button('OK', key='-OK-')]
        ]

        layout = [[sg.Column(coluna_pesquisar)]]

        janela_pesquisar = sg.Window('Pesquisar Registros', layout, resizable=False)

        while True:
            event, values = janela_pesquisar.read()
            if event == 'SAIR' or event == sg.WIN_CLOSED:
                break
            elif event == '-NOME_COMUNIDADES-':
                entrada = values['-NOME_COMUNIDADES-']
                sugestoes = funcoes_pesquisar.atualizar_sugestoes(entrada, funcoes_pesquisar.comunidades)

                if sugestoes:
                    janela_pesquisar['-SUGESTOES-'].update(sugestoes, visible=True)
                else:
                    janela_pesquisar['-SUGESTOES-'].update(visible=False)
            
            elif event == '-SUGESTOES-':
                selecao = values['-SUGESTOES-'][0]
                janela_pesquisar['-NOME_COMUNIDADES-'].update(selecao)
                janela_pesquisar['-SUGESTOES-'].update(visible=False)

            elif event == '-OK-' or event == '\r':
                nome_comunidade = values['-NOME_COMUNIDADES-']
                if nome_comunidade:
                    funcoes_pesquisar.pesquisar_por_nome_comunidade(nome_comunidade)
                else:
                    sg.popup('Por favor, digite o nome de uma comunidade.', title='Erro')
            elif event == 'Buscar Comunidade':
                funcoes_pesquisar.pesquisar_por_nome_comunidade(janela_pesquisar)


            elif event == '-MUNICIPIOS-':
                entrada = values['-MUNICIPIOS-']
                sugestoes = funcoes_pesquisar.atualizar_sugestoes(entrada, funcoes_pesquisar.municipios)

                if sugestoes:
                    janela_pesquisar['-SUGESTOES1-'].update(sugestoes, visible=True)
                else:
                    janela_pesquisar['-SUGESTOES1-'].update(visible=False)
            
            elif event == '-SUGESTOES1-':
                selecao = values['-SUGESTOES1-'][0]
                janela_pesquisar['-MUNICIPIOS-'].update(selecao)
                janela_pesquisar['-SUGESTOES1-'].update(visible=False)

            elif event == '-OK1-' or event == '\r':
                nome_municipio = values['-MUNICIPIOS-']
                if nome_municipio:
                    funcoes_pesquisar.pesquisar_por_nome_municipio(nome_municipio)
                else:
                    sg.popup('Por favor, digite o nome de um municipio.', title='Erro')
            elif event == 'Buscar Municipio':
                funcoes_pesquisar.pesquisar_por_nome_municipio(janela_pesquisar)

        janela_pesquisar.close()