#  SISREQ - Sistema de Regularização Quilombola

import PySimpleGUI as sg
import funcoes_registro
import salvar
import filtrar
import janela_pesquisar
import pesquisar
import constantes
import janela_consulta_graficos
import janela_consulta_relatorios
import datetime
import sys
from converter_xlsx_para_db import criar_janela_import
import pandas as pd

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

            elif event == 'IMPORTAR':
                criar_janela_import()

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
                janela_pesquisar.criar_janela_pesquisar(self.janela)

            elif event == 'Relatórios':
                janela_consulta_relatorios.criar_janela()

            elif event == 'Gráficos':
                janela_consulta_graficos.criar_janela()

            # Atualiza a lista conforme o usuário digita
            if event == '-MUNICIPIO-':
                nome_parcial = values['-MUNICIPIO-']
                if nome_parcial:
                    resultados = pesquisar.buscar_municipios_do_brasil(nome_parcial)
                    self.janela['-LIST-'].update(resultados)
                    self.janela['-LIST-'].update(visible=True)
                    self.janela['-OK3-'].update(visible=True)
                else:
                    self.janela['-LIST-'].update(visible=False)
                    self.janela['-OK3-'].update(visible=False)
            
            # Preenche o campo de entrada com o item selecionado e oculta a lista e o botão
            if event == '-LIST-':
                municipio_selecionado = values['-LIST-'][0]
                self.janela['-MUNICIPIO-'].update(municipio_selecionado)
                self.janela['-LIST-'].update(visible=False)
                self.janela['-OK3-'].update(visible=False)
            
            # Confirma a escolha do município
            if event == '-OK3-':
                municipio_selecionado = self.janela['-MUNICIPIO-'].get()
                self.janela['-LIST-'].update(visible=False)
                self.janela['-OK3-'].update(visible=False)

        self.janela.close()


    def criar_janela(self):
        conn = funcoes_registro.conectar_banco_de_dados()
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) as Total FROM SISREQ WHERE Numero")
        totalProcesso = cursor.fetchone()[0]

        sg.theme(constantes.JANELA_TEMA)

        coluna_1 = [
            [sg.Text('Número do\nProcesso:'), sg.Input(key='-NUMERO-', size=(21, 1))],
            [sg.CalendarButton('Data de Abertura', target='-DATA_ABERTURA-', key='-CALENDAR-', format='%d-%m-%Y'), sg.Input(size=(15, 1), key='-DATA_ABERTURA-', disabled=False)],
            [sg.Text('Comunidade:'), sg.Input(key='-NOME_COMUNIDADE-', size=(19, 1))],
            [sg.Text('Municípios:'), sg.Input(size=(20, 1), key='-MUNICIPIO-', enable_events=True), sg.Listbox(values=[], size=(20, 10), key='-LIST-', visible=False, enable_events=True), sg.Button("OK", key='-OK3-', visible=False)],
            [sg.Text('Número de\nFamílias:'), sg.Input(size=(21, 1), key='-NUM_FAMILIA-')]
        ]

        coluna_2 = [
            [sg.Text('Fase:'), sg.Combo(constantes.FASE_PROCESSO, size=(24, 6), key='-FASE_PROCESSO-')],
            [sg.Text('Etapa\nRTID:'), sg.Listbox(constantes.ETAPA_RTID, size=(24, 3), select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, key='-ETAPA_RTID-')],
            [sg.Text('Antropológico:'), sg.Combo(constantes.RELATORIO_ANTROPOLOGICO, size=(17, 6), key='-RA-')],
            [sg.Text('Certidão FCP:'), sg.Combo(constantes.CERTIFICACAO_FCP, size=(17, 6), key='-CERTIDAO-')],
            [sg.CalendarButton('Data de Certificação', target='-DATA_CERTIFICACAO-', key='-CALENDAR-', format='%d-%m-%Y'), sg.Input(size=(13, 1), key='-DATA_CERTIFICACAO-', disabled=False)]
        ]

        coluna_3 = [
            [sg.Text('Área\nIdentificada_ha:'), sg.Input(size=(10, 1), key='-AREA-')],
            [sg.Text('Área\nTitulada_ha:'), sg.Input(size=(13, 1), key='-TITULO-')],
            [sg.Text('PNRA\nQuilombola:'), sg.Combo(constantes.PNRA, size=(12, 1), key='-PNRA-')],
            [sg.Text('Latitude:  '), sg.Input(size=(15, 1), key='-LATITUDE-')],
            [sg.Text('Longitude:'), sg.Input(size=(15, 1), key='-LONGITUDE-')]
        ]

        coluna_4 = [
            [sg.Text('Edital DOU:'), sg.Input(size=(22, 1), key='-EDITAL_DOU-')],
            [sg.Text('Edital DOE:'), sg.Input(size=(22, 1), key='-EDITAL_DOE-')],
            [sg.CalendarButton('Portaria DOU', target='-PORTARIA_DOU-', key='-CALENDAR-', format='%d-%m-%Y'), sg.Input(size=(20, 1), key='-PORTARIA_DOU-', disabled=False)],
            [sg.CalendarButton('Decreto DOU', target='-DECRETO_DOU-', key='-CALENDAR-', format='%d-%m-%Y'), sg.Input(size=(20, 1), key='-DECRETO_DOU-', disabled=False)],
            [sg.Text('Sobreposição\nTerritorial:'), sg.Listbox(constantes.TIPO_SOBREPOSICAO, size=(22, 3), select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, key='-TIPO_SOBREPOSICAO-')]
        ]

        coluna_5 = [
            [sg.Text('Detalhes de\nSobreposição:'), sg.Multiline(size=(24, 2), key='-SOBREPOSICAO-')],
            [sg.Text('Ação Civil Pública:'), sg.Combo(constantes.ACAO_CIVIL_PUBLICA, size=(20, 1), key='-ACP-')],
            [sg.CalendarButton('Data da Sentença', target='-DATA_DECISAO-', key='-CALENDAR-', format='%d-%m-%Y'), sg.Input(size=(22, 1), key='-DATA_DECISAO-', disabled=False)],
            [sg.Text('Teor_Prazo da  \nSentença:'), sg.Multiline(size=(22, 2), key='-TEOR_DECISAO-')],
            [sg.Text('Outras Informações:'), sg.Multiline(size=(18, 2), key='-INFORMACAO-')]
        ]

        coluna_botoes = [
            [sg.Button('IMPORTAR', button_color='#ac4e04'), sg.Button('INSERIR', button_color='#ac4e04'), sg.Button('CONSULTAR', button_color='#ac4e04'), sg.Button('ALTERAR', button_color='#ac4e04'), sg.Button('PESQUISAR', button_color='#ac4e04'),]
        ]

        coluna_botoes_relatorios_e_graficos= [
            [sg.Button('Relatórios', button_color='#ac4e04'), sg.Button('Gráficos', button_color='#ac4e04'), sg.VerticalSeparator(), sg.Text('EXTRAIR:', font=constantes.FONTE), sg.Button('Planilha', button_color='#ac4e04')],
        ]

        coluna_total_processos = [
            [sg.Text(f"{totalProcesso} Processos", key='total_processo', font='Any 10 bold', text_color='black', background_color='#c8cf9d')]
        ]

        layout = [
            [sg.Text('CADASTRO DE PROCESSOS', font=constantes.FONTE)],
            [sg.Column(coluna_1), sg.VerticalSeparator(), sg.Column(coluna_2), sg.VerticalSeparator(), sg.Column(coluna_3), sg.VerticalSeparator(), sg.Column(coluna_4), sg.VerticalSeparator(), sg.Column(coluna_5)],
            [sg.Text('REGISTROS:', font=constantes.FONTE), sg.Column(coluna_botoes), sg.VerticalSeparator(), sg.Text('CONSULTAR:', font=constantes.FONTE), sg.Column(coluna_botoes_relatorios_e_graficos), sg.VerticalSeparator(), sg.Text('TOTAL:', font=constantes.FONTE), sg.Column(coluna_total_processos)],
            [sg.Text('FILTRAR POR FASE:', font=constantes.FONTE), sg.Button('Inicial', button_color='green'), sg.Button('RTID', button_color='green'), sg.Button('Publicação', button_color='green'), sg.Button('Notificação', button_color='green'), sg.Button('Contestação', button_color='green'), sg.Button('Recurso', button_color='green'), sg.Button('Portaria', button_color='green'), sg.Button('Decreto', button_color='green'), sg.Button('Desapropriação', button_color='green'), sg.Button('Titulação', button_color='green'), sg.Button('Desintrusão', button_color='green')],
            [sg.Table(
                values=[],
                headings=[
                    'ID ', '    Numero   ', 'Data_Abertura', '  Comunidade  ', '  Municipio  ', ' Area_ha ',
                    'Num_familias', 'Fase_Processo', ' Etapa_RTID ', ' Edital_DOU ', 'Edital_DOE',
                    'Portaria_DOU', 'Decreto_DOU', 'Area_ha_Titulada', '  PNRA   ', 'Relatorio_Antropologico',
                    'Latitude', 'Longitude', 'Certidao_FCP', 'Data_Certificacao', '  Sobreposicao  ',
                    'Analise_de_Sobreposicao', 'Acao_Civil_Publica', 'Data_Decisao', 'Teor_Decisao_Prazo_Sentença',
                    '          Outras_Informacoes'
                ],
                num_rows=22,
                key='-TABLE-',
                hide_vertical_scroll=False,
                vertical_scroll_only=False,
                justification='left',
                auto_size_columns=True,
            )],
            
            [sg.Text('', size=(68, 1)), constantes.JANELA_RODAPE, sg.Text('', size=(0, 1))]
        ]

        janela = sg.Window("                                                                                                                                                                         SISREQ - Sistema de Regularização Quilombola (v.1.1.0)", layout, size=(1400, 800), resizable=True)
        return janela


def check_license():
    today = datetime.datetime.now().date()

    expiration_date = datetime.datetime.strptime("2025-05-15", "%Y-%m-%d").date()  # prazo da licença

    if today > expiration_date:
        sg.popup_error("Licença expirada.", "Entre em contato para renovar:", "Whatsapp => (98) 98895-7452", "Email => michaeljmc@outlook.com.br", 
                    title="Aviso", 
                    font=constantes.FONTE_DE_AVSIO)
        
        sys.exit(1)
    
    if today == expiration_date:
        sg.popup("Sua licença expira hoje.", "Entre em contato para renovar:", "Whatsapp => (98) 98895-7452", "Email => michaeljmc@outlook.com.br", 
                title="Aviso", 
                font=constantes.FONTE_DE_AVSIO)
       
    else:
        None