#  SISREQ - Sistema de Regularização Quilombola

import PySimpleGUI as sg
import funcoes_registro
import salvar
import filtrar
import pesquisar
import constantes
import janela_consulta_graficos
import janela_consulta_relatorios

class Aplicacao:
    def __init__(self):
        self.janela = self.criar_janela()

    def iniciar(self):
        while True:
            event, values = self.janela.read()

            conn = funcoes_registro.conectar_banco_de_dados()
            cursor = conn.cursor()

            cursor.execute("SELECT COUNT(*) as Total FROM SISREQ WHERE Numero")
            totalProcesso = cursor.fetchone()[0]
            
            if event == sg.WIN_CLOSED:
                break

            elif event == 'INSERIR':
                funcoes_registro.inserir_dados(values, self.janela)
                totalProcesso += 1
                self.janela['total_processo'].update(f'{totalProcesso} Processos')
                
                funcoes_registro.consultar_registros(self.janela)

            elif event == 'CONSULTAR':
                funcoes_registro.consultar_registros(self.janela)
                self.janela['total_processo'].update(f'{totalProcesso} Processos')

            elif event == 'ALTERAR':
                funcoes_registro.alterar_registro(self.janela)

            elif event == 'Planilha':
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

            elif event == 'PESQUISAR':
                self.criar_janela_pesquisar()

            elif event == 'Relatórios':
                janela_consulta_relatorios.criar_janela()

            elif event == 'Gráficos':
                janela_consulta_graficos.criar_janela()

            # Evento de digitação no campo de entrada comunidade
            elif event == '-NOME_COMUNIDADES-':
                entrada = values['-NOME_COMUNIDADES-']
                sugestoes = pesquisar.atualizar_sugestoes(entrada, pesquisar.comunidades)

                if sugestoes:
                    self.janela['-SUGESTOES-'].update(sugestoes, visible=True)
                else:
                    self.janela['-SUGESTOES-'].update(visible=False)

            # Evento de seleção na lista de sugestões comunidade
            if event == '-SUGESTOES-':
                selecao = values['-SUGESTOES-'][0]
                self.janela['-NOME_COMUNIDADES-'].update(selecao)
                self.janela['-SUGESTOES-'].update(visible=False)

            # Evento do botão OK
            if event == '-OK-':
                nome_comunidade = values['-NOME_COMUNIDADES-']
                if nome_comunidade:
                    pesquisar.pesquisar_por_nome_comunidade(nome_comunidade)
                else:
                    sg.popup('Por favor, digite o nome de uma comunidade.', title='Erro')

            elif event == 'Buscar Comunidade':
                pesquisar.pesquisar_por_nome_comunidade(self.janela)
            
            # Evento de digitação no campo de entrada municipio
            elif event == '-MUNICIPIOS-':
                entrada = values['-MUNICIPIOS-']
                sugestoes = pesquisar.atualizar_sugestoes(entrada, pesquisar.municipios)

                if sugestoes:
                    self.janela['-SUGESTOES-'].update(sugestoes, visible=True)
                else:
                    self.janela['-SUGESTOES-'].update(visible=False)

            # Evento de seleção na lista de sugestões municipio
            if event == '-SUGESTOES-':
                selecao = values['-SUGESTOES-'][0]
                self.janela['-MUNICIPIOS-'].update(selecao)
                self.janela['-SUGESTOES-'].update(visible=False)

            # Evento do botão OK
            if event == '-OK-':
                nome_municipio = values['-MUNICIPIOS-']
                if nome_municipio:
                    pesquisar.pesquisar_por_nome_municipio(nome_municipio)
                else:
                    sg.popup('Por favor, digite o nome de um município.', title='Erro')

            elif event == 'Buscar Municipio':
                pesquisar.pesquisar_por_nome_municipio(self.janela)

             # Evento de digitação no campo de entrada processo
            elif event == '-NUMEROS-':
                entrada = values['-NUMEROS-']
                sugestoes = pesquisar.atualizar_sugestoes(entrada, pesquisar.processos)

                if sugestoes:
                    self.janela['-SUGESTOES-'].update(sugestoes, visible=True)
                else:
                    self.janela['-SUGESTOES-'].update(visible=False)

            # Evento de seleção na lista de sugestões processo
            if event == '-SUGESTOES-':
                selecao = values['-SUGESTOES-'][0]
                self.janela['-NUMEROS-'].update(selecao)
                self.janela['-SUGESTOES-'].update(visible=False)

            # Evento do botão OK
            if event == '-OK2-':
                num_processo = values['-NUMEROS-']
                if num_processo:
                    pesquisar.pesquisar_por_num_processo(num_processo)
                else:
                    sg.popup('Por favor, digite o número de um processo.', title='Erro')

            elif event == 'Buscar Processo':
                pesquisar.pesquisar_por_num_processo(self.janela)

        self.janela.close()


    def criar_janela(self):
        conn = funcoes_registro.conectar_banco_de_dados()
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) as Total FROM SISREQ WHERE Numero")
        totalProcesso = cursor.fetchone()[0]

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
            [sg.Button('INSERIR', button_color='#ac4e04'), sg.Button('CONSULTAR', button_color='#ac4e04'), sg.Button('ALTERAR', button_color='#ac4e04'), sg.Button('PESQUISAR', button_color='#ac4e04'),]
        ]

        coluna_botoes_relatorios_e_graficos= [
            [sg.Button('Relatórios', button_color='#ac4e04'), sg.Button('Gráficos', button_color='#ac4e04'), sg.VerticalSeparator(), sg.Text('EXTRAIR:', font='Helvetica 10 bold'), sg.Button('Planilha', button_color='#ac4e04')],
        ]

        coluna_total_processos = [
            [sg.Text(f"{totalProcesso} Processos", key='total_processo', font='Any 10 bold', text_color='black', background_color='#c8cf9d')]
        ]

        layout = [
            [sg.Text(' ', size=(75, 1)), sg.Text('CADASTRO DE PROCESSOS', font='Helvetica 10 bold')],
            [sg.Column(coluna_1), sg.VerticalSeparator(), sg.Column(coluna_2), sg.VerticalSeparator(), sg.Column(coluna_3), sg.VerticalSeparator(), sg.Column(coluna_4), sg.VerticalSeparator(), sg.Column(coluna_5)],
            [sg.Text('REGISTROS:', font='Helvetica 10 bold'), sg.Column(coluna_botoes), sg.VerticalSeparator(), sg.Text('CONSULTAR:', font='Helvetica 10 bold'), sg.Column(coluna_botoes_relatorios_e_graficos), sg.VerticalSeparator(), sg.Text('TOTAL:', font='Helvetica 10 bold'), sg.Column(coluna_total_processos)],
            [sg.Text('FILTRAR POR FASE:', font='Helvetica 10 bold'), sg.Button('Inicial', button_color='green'), sg.Button('RTID', button_color='green'), sg.Button('Publicação', button_color='green'), sg.Button('Notificação', button_color='green'), sg.Button('Contestação', button_color='green'), sg.Button('Recurso', button_color='green'), sg.Button('Portaria', button_color='green'), sg.Button('Decreto', button_color='green'), sg.Button('Desapropriação', button_color='green'), sg.Button('Titulação', button_color='green'), sg.Button('Desintrusão', button_color='green')],
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
                num_rows=24,
                key='-TABLE-',
                hide_vertical_scroll=False,
                vertical_scroll_only=False,
                justification='left',
                auto_size_columns=True,
            )],

            
            [sg.Text('', size=(75, 1)), constantes.JANELA_RODAPE, sg.Text('', size=(0, 1))]
        ]

        janela = sg.Window("SISREQ - Sistema de Regularização Quilombola (v.1.1.0)", layout, resizable=True)
        return janela
    

    def criar_janela_pesquisar(self):
        coluna_pesquisar = [
            [sg.Text('Pesquisar Comunidade:', font='Helvetica 10 bold'), sg.Input(size=(25, 1), key='-NOME_COMUNIDADES-', enable_events=True), sg.Listbox(values=[], size=(25, 4), key='-SUGESTOES-', enable_events=True, visible=False), sg.Button('OK', key='-OK-', button_color='#3169F5')],
            [sg.Text(' ')],
            [sg.Text('Pesquisar Município:    ', font='Helvetica 10 bold'), sg.Input(size=(25, 1), key='-MUNICIPIOS-', enable_events=True), sg.Listbox(values=[], size=(25, 4), key='-SUGESTOES1-', enable_events=True, visible=False), sg.Button('OK', key='-OK1-', button_color='#3169F5')],
            [sg.Text(' ')],
            [sg.Text('Pesquisar Processo:    ', font='Helvetica 10 bold'), sg.Input(size=(25, 1), key='-NUMEROS-', enable_events=True), sg.Listbox(values=[], size=(25, 4), key='-SUGESTOES2-', enable_events=True, visible=False), sg.Button('OK', key='-OK2-', button_color='#3169F5')],
            [sg.Text(' ')]
        ]

        layout = [[sg.Column(coluna_pesquisar)]]

        janela_pesquisar = sg.Window('Buscar Registros', layout, resizable=False)

        while True:
            event, values = janela_pesquisar.read()
            if event == sg.WIN_CLOSED:
                break

            elif event == '-NOME_COMUNIDADES-':
                entrada = values['-NOME_COMUNIDADES-']
                sugestoes = pesquisar.atualizar_sugestoes(entrada, pesquisar.comunidades)

                if sugestoes:
                    janela_pesquisar['-SUGESTOES-'].update(sugestoes, visible=True)
                else:
                    janela_pesquisar['-SUGESTOES-'].update(visible=False)
            
            elif event == '-SUGESTOES-':
                selecao = values['-SUGESTOES-'][0]
                janela_pesquisar['-NOME_COMUNIDADES-'].update(selecao)
                janela_pesquisar['-SUGESTOES-'].update(visible=False)

            elif event == '-OK-':
                nome_comunidade = values['-NOME_COMUNIDADES-']
                if nome_comunidade:
                    pesquisar.pesquisar_por_nome_comunidade(nome_comunidade)
                else:
                    sg.popup('Por favor, digite o nome de uma comunidade.', title='Erro', font='Helvetica 10 bold')

            elif event == 'Buscar Comunidade':
                pesquisar.pesquisar_por_nome_comunidade(janela_pesquisar)


            elif event == '-MUNICIPIOS-':
                entrada = values['-MUNICIPIOS-']
                sugestoes = pesquisar.atualizar_sugestoes(entrada, pesquisar.municipios)

                if sugestoes:
                    janela_pesquisar['-SUGESTOES1-'].update(sugestoes, visible=True)
                else:
                    janela_pesquisar['-SUGESTOES1-'].update(visible=False)
            
            elif event == '-SUGESTOES1-':
                selecao = values['-SUGESTOES1-'][0]
                janela_pesquisar['-MUNICIPIOS-'].update(selecao)
                janela_pesquisar['-SUGESTOES1-'].update(visible=False)

            elif event == '-OK1-':
                nome_municipio = values['-MUNICIPIOS-']
                if nome_municipio:
                    pesquisar.pesquisar_por_nome_municipio(nome_municipio)
                else:
                    sg.popup('Por favor, digite o nome de um municipio.', title='Erro', font='Helvetica 10 bold')

            elif event == 'Buscar Municipio':
                pesquisar.pesquisar_por_nome_municipio(janela_pesquisar)
            
            elif event == '-NUMEROS-':
                entrada = values['-NUMEROS-']
                sugestoes = pesquisar.atualizar_sugestoes(entrada, pesquisar.processos)

                if sugestoes:
                    janela_pesquisar['-SUGESTOES2-'].update(sugestoes, visible=True)
                else:
                    janela_pesquisar['-SUGESTOES2-'].update(visible=False)
            
            elif event == '-SUGESTOES2-':
                selecao = values['-SUGESTOES2-'][0]
                janela_pesquisar['-NUMEROS-'].update(selecao)
                janela_pesquisar['-SUGESTOES2-'].update(visible=False)

            elif event == '-OK2-':
                num_processo = values['-NUMEROS-']
                if num_processo:
                    pesquisar.pesquisar_por_num_processo(num_processo)
                else:
                    sg.popup('Por favor, digite o número de um processo.', title='Erro', font='Helvetica 10 bold')
                    
            elif event == 'Buscar Processo':
                pesquisar.pesquisar_por_num_processo(janela_pesquisar)

        janela_pesquisar.close()