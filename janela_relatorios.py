import PySimpleGUI as sg
import constantes
import relatorios

def criar_janela():
        sg.theme(constantes.JANELA_TEMA)

        coluna_relatorios = [
            [sg.Button('Número de Famílias', button_color='green')],
            [sg.Button('Área Total', button_color='green')],
            [sg.Button('Territórios Identificados', button_color='green')],
            [sg.Button('Territórios Não-Identificados', button_color='green')],
            [sg.Button('Ações Judiciais', button_color='green')],
            [sg.Button('TQ em PA', button_color='green')]
        ]

        layout = [[sg.Column(coluna_relatorios)]]

        janela_relatorios = sg.Window('Exibir Relatórios', layout, resizable=False)

        while True:
            event, values = janela_relatorios.read()
            if event == 'SAIR' or event == sg.WIN_CLOSED:
                break
            elif event == 'Número de Famílias':
                relatorios.exibir_total_de_familias()
            elif event == 'Área Total':
                relatorios.exibir_area_total()
            elif event == 'TQ em PA':
                relatorios.exibir_territorios_quilombolas_em_assentamentos()
            elif event == 'Territórios Identificados':
                relatorios.territorios_identificados()
            elif event == 'Territórios Não-Identificados':
                relatorios.territorios_nao_identificados()
            elif event == 'Ações Judiciais':
                relatorios.exibir_processos_com_acao_judicial()
            
        return janela_relatorios