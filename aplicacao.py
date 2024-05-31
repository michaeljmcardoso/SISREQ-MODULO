import PySimpleGUI as sg
import funcoes
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
                funcoes.inserir_dados(values, self.janela)
                funcoes.consultar_registros(self.janela)
            elif event == 'CONSULTAR':
                funcoes.consultar_registros(self.janela)

        self.janela.close()

    def criar_janela(self):
        sg.theme('Darkgreen')
        layout = [
            [sg.Text('Nome:'), sg.Input(key='-NOME-', size=(20, 1))], 
            [sg.Text('Email: '), sg.Input(key='-EMAIL-', size=(20, 1))],
            [sg.Text('Senha:'), sg.Input(key='-SENHA-', size=(20, 1))],
            [sg.Button('INSERIR', button_color='#ac4e04'), sg.Button('CONSULTAR', button_color='green')],
            [sg.Table(
            values=[],
            headings=[
                'ID',
                '      Nome      ',
                '      Email      ',
                '  Senha  '
            ],
            num_rows=25,
            key='-TABLE-',
            hide_vertical_scroll=False,
            vertical_scroll_only=False,
            justification='left',
            auto_size_columns=True,
            )],

            [sg.Button('SAIR', button_color='#ac4e04')],

            [sg.Text('', size=(15, 1)), constantes.JANELA_RODAPE, sg.Text('', size=(15, 1))]
            ]

        janela = sg.Window("SISREQ - Sistema de Regularização Quilombola (v.1.1.0)", layout, resizable=True)
        return janela