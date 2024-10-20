""" SISREQ - Sistema de Regularização Quilombola
Módulo de Consulta """

import PySimpleGUI as sg
import funcoes
import constantes
import filtrar
from salvar import salvar_planilha
from janela_pesquisas import criar_janela_pesquisar
from pesquisar import buscar_municipios_do_brasil
from janela_consulta_graficos import criar_janela_graficos
from janela_consulta_relatorios import criar_janela_relatorios
from converter_xlsx_para_db import criar_janela_import

class Aplicacao:
    def __init__(self):
        self.janela = self.criar_janela()

    def iniciar(self):
        while True:
            event, values = self.janela.read()

            conn = funcoes.conectar_banco_de_dados()
            cursor = conn.cursor()

            cursor.execute("SELECT COUNT(*) as Total FROM SISREQ WHERE Numero")
            totalProcesso = cursor.fetchone()[0]
            
            if event == sg.WIN_CLOSED:
                break

            elif event == 'IMPORTAR':
                criar_janela_import()

            elif event == 'VISÃO GERAL':
                funcoes.visao_geral(self.janela)
                self.janela['total_processo'].update(f'{totalProcesso} Processos')

            elif event == 'CONSULTAR':
                funcoes.consultar_registro(self.janela)

            elif event == 'Planilha':
                salvar_planilha(self.janela)

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
                criar_janela_pesquisar(self.janela)

            elif event == 'Relatórios':
                criar_janela_relatorios()

            elif event == 'Gráficos':
                criar_janela_graficos()

            # Atualiza a lista conforme o usuário digita
            if event == '-MUNICIPIO-':
                nome_parcial = values['-MUNICIPIO-']
                if nome_parcial:
                    resultados = buscar_municipios_do_brasil(nome_parcial)
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
        conn = funcoes.conectar_banco_de_dados()
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) as Total FROM SISREQ WHERE Numero")
        totalProcesso = cursor.fetchone()[0]

        sg.theme(constantes.JANELA_TEMA)
        
        coluna_botoes = [
            [sg.Button('VISÃO GERAL', button_color='#ac4e04'), sg.Button('CONSULTAR', button_color='#ac4e04'), sg.Button('PESQUISAR', button_color='#ac4e04'), sg.Button('IMPORTAR', button_color='#ac4e04')]
        ]

        coluna_botoes_relatorios_e_graficos= [
            [sg.Button('Relatórios', button_color='#ac4e04'), sg.Button('Gráficos', button_color='#ac4e04'), sg.VerticalSeparator(), sg.Text('EXTRAIR:', font=constantes.FONTE), sg.Button('Planilha', button_color='#ac4e04')],
        ]

        coluna_total_processos = [
            [sg.Text(f"{totalProcesso} Processos", key='total_processo', font='Any 10 bold', text_color='black', background_color='#c8cf9d')]
        ]

        layout = [
            [sg.Text('REGISTROS:', font=constantes.FONTE), sg.Column(coluna_botoes), sg.VerticalSeparator(), sg.Text('CONSULTAR:', font=constantes.FONTE), sg.Column(coluna_botoes_relatorios_e_graficos), sg.VerticalSeparator(), sg.Text('TOTAL:', font=constantes.FONTE), sg.Column(coluna_total_processos)],
            [sg.Text('FILTRAR POR FASE:', font=constantes.FONTE), sg.Button('Inicial', button_color='green'), sg.Button('RTID', button_color='green'), sg.Button('Publicação', button_color='green'), sg.Button('Notificação', button_color='green'), sg.Button('Contestação', button_color='green'), sg.Button('Recurso', button_color='green'), sg.Button('Portaria', button_color='green'), sg.Button('Decreto', button_color='green'), sg.Button('Desapropriação', button_color='green'), sg.Button('Titulação', button_color='green'), sg.Button('Desintrusão', button_color='green')],
            [sg.Table(
                values=[],
                headings=constantes.headings,
                num_rows=33,
                key='-TABLE-',
                hide_vertical_scroll=False,
                vertical_scroll_only=False,
                justification='left',
                auto_size_columns=True,
                header_text_color='white',  # Cor do texto dos cabeçalhos
                header_background_color='blue'  # Cor de fundo dos cabeçalhos
            )
            ],
            [sg.Text('', size=(68, 1)), constantes.JANELA_RODAPE, sg.Text('', size=(0, 1))]
        ]

        janela = sg.Window("                                                                                                                                     SISREQ - SISTEMA DE REGULARIZAÇÃO QUILOMBOLA (v.1.2.0) - MÓDULO DE CONSULTA", layout, size=(1400, 800), resizable=True)
        return janela