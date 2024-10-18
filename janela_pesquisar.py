import PySimpleGUI as sg
import pesquisar
from constantes import FONTE

def criar_janela_pesquisar(janela_pesquisar):
        coluna_pesquisar = [
            [sg.Text('Pesquisar Comunidade:', font=FONTE), sg.Input(size=(25, 1), key='-NOME_COMUNIDADES-', enable_events=True), sg.Listbox(values=[], size=(25, 4), key='-SUGESTOES-', enable_events=True, visible=False), sg.Button('OK', key='-OK-', button_color='#3169F5')],
            [sg.Text(' ')],
            [sg.Text('Pesquisar Município:    ', font=FONTE), sg.Input(size=(25, 1), key='-MUNICIPIOS-', enable_events=True), sg.Listbox(values=[], size=(25, 4), key='-SUGESTOES1-', enable_events=True, visible=False), sg.Button('OK', key='-OK1-', button_color='#3169F5')],
            [sg.Text(' ')],
            [sg.Text('Pesquisar Processo:    ', font=FONTE), sg.Input(size=(25, 1), key='-NUMEROS-', enable_events=True), sg.Listbox(values=[], size=(25, 4), key='-SUGESTOES2-', enable_events=True, visible=False), sg.Button('OK', key='-OK2-', button_color='#3169F5')],
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
                    sg.popup('Por favor, digite o nome de uma comunidade.', title='Erro', font=FONTE)
            
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
                    sg.popup('Por favor, digite o nome de um municipio.', title='Erro', font=FONTE)
          
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
                    sg.popup('Por favor, digite o número de um processo.', title='Erro', font=FONTE)
            
        janela_pesquisar.close()