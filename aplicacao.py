import PySimpleGUI as sg
import funcoesRegistro
import funcoesPlanilha
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
                funcoesRegistro.inserir_dados(values, self.janela)
                funcoesRegistro.consultar_registros(self.janela)
            elif event == 'CONSULTAR':
                funcoesRegistro.consultar_registros(self.janela)
            elif event == 'ALTERAR':
                funcoesRegistro.alterar_registro(self.janela)
            elif event == 'Extrair Planilha':
                funcoesPlanilha.extrair_planilha(self.janela)

        self.janela.close()

    def criar_janela(self):
        sg.theme('Darkgreen')

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

        layout = [
            [sg.Column(coluna_1), sg.VerticalSeparator(), 
             sg.Column(coluna_2), sg.VerticalSeparator(), 
             sg.Column(coluna_3), sg.VerticalSeparator(),
             sg.Column(coluna_4), sg.VerticalSeparator(), 
             sg.Column(coluna_5)
            ],

            [sg.Button('INSERIR', button_color='#ac4e04'), sg.Button('CONSULTAR', button_color='green'), sg.Button('ALTERAR', button_color='#ac4e04'), sg.Button('Extrair Planilha', button_color='green')],
            
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

            [sg.Text('', size=(75, 1)), constantes.JANELA_RODAPE, sg.Text('', size=(0, 1))]
        ]

        janela = sg.Window("SISREQ - Sistema de Regularização Quilombola (v.1.1.0)", layout, resizable=True)
        return janela
    
