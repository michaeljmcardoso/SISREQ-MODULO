import PySimpleGUI as sg
import constantes
import graficos

def criar_janela():
        sg.theme(constantes.JANELA_TEMA)

        coluna_graficos = [
            [sg.Button('Andamento de Processos', button_color='blue', font=constantes.FONTE)],
            [sg.Text(' ')],
            [sg.Button('Processos por Fase', button_color='blue', font=constantes.FONTE)],
            [sg.Text(' ')],
            [sg.Button('Ação Civil Pública', button_color='blue', font=constantes.FONTE)],
            [sg.Text(' ')],
            [sg.Button('Sobreposições', button_color='blue', font=constantes.FONTE)],
            [sg.Text(' ')],
            [sg.Button('Relatórios Antropológicos', button_color='blue', font=constantes.FONTE)],
            [sg.Text(' ')],
            [sg.Button('Ano de Abertura', button_color='blue', font=constantes.FONTE)],
            [sg.Text(' ')],
            [sg.Button('Distrubuição por Municípios', button_color='blue', font=constantes.FONTE)],
            [sg.Text(' ')],
            [sg.Button('Geolocalização', button_color='blue', font=constantes.FONTE)],
            [sg.Text(' ')]
        ]

        layout = [[sg.Column(coluna_graficos)]]

        janela_graficos = sg.Window('Exibir Gráficos', layout, resizable=False)

        while True:
            event, values = janela_graficos.read()
            if event == sg.WIN_CLOSED:
                break

            elif event == 'Distrubuição por Municípios':
                graficos.exibir_processos_por_municipio()

            elif event == 'Ano de Abertura':
                graficos.exibir_processos_por_data_abertura()

            elif event == 'Ação Civil Pública':
                graficos.exibir_processos_com_acao_civil()

            elif event == 'Andamento de Processos':
                graficos.exibir_andamento_de_processos()

            elif event == 'Processos por Fase':
                graficos.exibir_processos_por_fase_atual()

            elif event == 'Sobreposições':
                graficos.exibir_tipo_de_sopreposicao()

            elif event == 'Relatórios Antropológicos':
                graficos.exibir_relatorios_antropologicos_por_forma_de_elaboracao()
                
            elif event == 'Geolocalização':
                graficos.plotar_mapa_interativo()
                
        return janela_graficos