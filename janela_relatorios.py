import PySimpleGUI as sg
import constantes
import relatorios

def criar_janela():
        sg.theme(constantes.JANELA_TEMA)

        coluna_relatorios = [
            [sg.Button('RTID´s Publicados', button_color='blue')],
            [sg.Button('Titulos Expedidos', button_color='blue')],
            [sg.Button('Territórios Identificados', button_color='blue')],
            [sg.Button('Territórios Não-Identificados', button_color='blue')],
            [sg.Button('Quilombolas em Assentamentos', button_color='blue')],
            [sg.Button('Total de Famílias', button_color='blue')],
            [sg.Button('Área Total', button_color='blue')],
            [sg.Button('Ações Judiciais', button_color='blue')],
            
        ]

        layout = [[sg.Column(coluna_relatorios)]]

        janela_relatorios = sg.Window('Exibir Relatórios', layout, resizable=False)

        while True:
            event, values = janela_relatorios.read()
            if event == 'SAIR' or event == sg.WIN_CLOSED:
                break

            elif event == 'RTID´s Publicados':
                relatorios.rtids_publicados()
            
            elif event == 'Titulos Expedidos':
                relatorios.titulos_expedidos()

            elif event == 'Total de Famílias':
                relatorios.exibir_total_de_familias()

            elif event == 'Área Total':
                relatorios.exibir_area_total()

            elif event == 'Quilombolas em Assentamentos':
                relatorios.exibir_territorios_quilombolas_em_assentamentos()

            elif event == 'Territórios Identificados':
                relatorios.territorios_identificados()

            elif event == 'Territórios Não-Identificados':
                relatorios.territorios_nao_identificados()

            elif event == 'Ações Judiciais':
                relatorios.exibir_processos_com_acao_judicial()
            
        return janela_relatorios