import PySimpleGUI as sg
import relatorios
from constantes import FONTE, JANELA_TEMA

def criar_janela_relatorios():
        sg.theme(JANELA_TEMA)

        coluna_relatorios = [
            [sg.Button('RTID´s Publicados', button_color='blue', font=FONTE)],
            [sg.Text(' ')],
            [sg.Button('Titulos Expedidos', button_color='blue', font=FONTE)],
            [sg.Text(' ')],
            [sg.Button('Territórios Identificados', button_color='blue', font=FONTE)],
            [sg.Text(' ')],
            [sg.Button('Territórios Não-Identificados', button_color='blue', font=FONTE)],
            [sg.Text(' ')],
            [sg.Button('Quilombos em Assentamentos', button_color='blue', font=FONTE)],
            [sg.Text(' ')],
            [sg.Button('Total de Famílias', button_color='blue', font=FONTE)],
            [sg.Text(' ')],
            [sg.Button('Área Total', button_color='blue', font=FONTE)],
            [sg.Text(' ')],
            [sg.Button('Ações Civis Públicas', button_color='blue', font=FONTE)],
            [sg.Text(' ')],
            [sg.Button('Certificação FCP', button_color='blue', font=FONTE)],
            [sg.Text(' ')],
            [sg.Button('Cadastro PNRA', button_color='blue', font=FONTE)]
            
        ]

        layout = [[sg.Column(coluna_relatorios)]]

        janela_relatorios = sg.Window('EXIBIR RELATÓRIOS', layout, resizable=False, finalize=True)

        while True:
            event, values = janela_relatorios.read()
            if event == sg.WIN_CLOSED:
                break

            elif event == 'RTID´s Publicados':
                relatorios.rtids_publicados()
            
            elif event == 'Titulos Expedidos':
                relatorios.titulos_expedidos()

            elif event == 'Total de Famílias':
                relatorios.exibir_total_de_familias()

            elif event == 'Área Total':
                relatorios.exibir_area_total()

            elif event == 'Quilombos em Assentamentos':
                relatorios.exibir_territorios_quilombolas_em_assentamentos()

            elif event == 'Territórios Identificados':
                relatorios.territorios_identificados()

            elif event == 'Territórios Não-Identificados':
                relatorios.territorios_nao_identificados()

            elif event == 'Ações Civis Públicas':
                relatorios.exibir_processos_com_acao_judicial()
            
            elif event == 'Certificação FCP':
                relatorios.exibir_comunidades_sem_certificacao()
            
            elif event == 'Cadastro PNRA':
                relatorios.cadastro_pnra()
            
        return janela_relatorios