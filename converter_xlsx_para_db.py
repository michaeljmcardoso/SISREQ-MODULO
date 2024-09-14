import os
import sys
import pandas as pd
import sqlite3
import PySimpleGUI as sg
import constantes


def criar_janela_import():
        janela = [
            [sg.Text("Selecione o arquivo Excel (.xlsx):", font=constantes.FONTE), sg.InputText(), sg.FileBrowse(file_types=(("Excel Files", "*.xlsx"),), button_color='#3169F5', font=constantes.FONTE)],
            [sg.Button("Converter", button_color='green', font=constantes.FONTE), sg.Button("Fechar", button_color='#ac4e04', font=constantes.FONTE)],
            [sg.Text(' ')],
            [sg.Text(' ', size=(20, 1)), sg.Text(f"Sistema de Regularização Quilombola - SISREQ. © {constantes.ANO_ATUAL}\n                 Todos os direitos reservados.", text_color='black', font='Helvetica 8 bold')],
        ]

        # Tema
        sg.theme(constantes.JANELA_TEMA)

        # Criar a janela
        janela_converter = sg.Window("Conversor de Planilha para Banco de Dados", janela)

        # Loop de eventos para processar ações do usuário
        while True:
            event, values = janela_converter.read()

            if event == sg.WIN_CLOSED or event == "Fechar":
                break

            if event == "Converter":
                xlsx_file_path = values[0]
                if not xlsx_file_path:
                    sg.popup("Por favor, selecione um arquivo Excel.", title="Aviso", icon=sg.POPUP_BUTTONS_ERROR)
                else:
                    convert_xlsx_to_db(xlsx_file_path)

        # Fechar a janela
        janela_converter.close()
        

# Função para reiniciar o programa
def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def convert_xlsx_to_db(xlsx_file_path):
    try:
        # Definir o caminho fixo para o arquivo .db
        sqlite_db_path = "sisreq.db"

        # Verificar se o banco de dados já existe e tentar apagar a tabela, sem remover o arquivo
        conn = sqlite3.connect(sqlite_db_path)
        conn.execute("DROP TABLE IF EXISTS SISREQ")
        conn.close()
        
        # Verificar se o banco de dados já existe. Se sim, apagar o arquivo existente
        #if os.path.exists(sqlite_db_path):
        #    os.remove(sqlite_db_path)

        # Carregar o arquivo Excel (.xlsx)
        df_excel = pd.read_excel(xlsx_file_path)

        # Substituir None (NaN) por campos vazios
        df_excel = df_excel.fillna('')

        # Conectar ao banco de dados SQLite
        conn = sqlite3.connect(sqlite_db_path)

        # Definir a tabela no banco de dados com a estrutura solicitada
        create_table_query = """
        CREATE TABLE IF NOT EXISTS SISREQ (
            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            Numero TEXT,
            Data_Abertura DATE,
            Comunidade TEXT,
            Municipio TEXT,
            Area_ha NUMERIC,
            Num_familias NUMERIC,
            Fase_Processo TEXT,
            Etapa_RTID TEXT,
            Edital_DOU TEXT,
            Edital_DOE TEXT,
            Portaria_DOU DATE,
            Decreto_DOU DATE,
            Area_ha_Titulada NUMERIC,
            PNRA TEXT,
            Relatorio_Antropologico TEXT,
            Latitude NUMERIC,
            Longitude NUMERIC,
            Certidao_FCP TEXT,
            Data_Certificacao DATE,
            Sobreposicao TEXT,
            Analise_de_Sobreposicao TEXT,
            Acao_Civil_Publica TEXT,
            Data_Decisao DATE,
            Teor_Decisao_Prazo_Sentença TEXT,
            Outras_Informacoes TEXT
        );
        """

        # Criar a tabela
        conn.execute(create_table_query)

        # Inserir os dados da planilha Excel na tabela
        df_excel.to_sql('SISREQ', conn, if_exists='append', index=False)

        # Fechar a conexão com o banco de dados
        conn.commit()
        conn.close()

        sg.popup_notify(
            f"Banco de dados '{sqlite_db_path}' criado com sucesso!", 
            "Seu arquivo foi salvo e já pode ser acessado pelo SISREQ.",
            "Aguarde enquanto reiniciamos o programa.",
            "Aperte CONSULTAR na janela principal para atualizar a Tabela.", 
            title="Sucesso", display_duration_in_ms=12000, fade_in_duration=2.0
            )
        
        restart_program()

    except FileNotFoundError as e:
        sg.popup_error(f"O arquivo '{xlsx_file_path}' não foi encontrado. {e}", 
                       font=constantes.FONTE, title="Erro")
    except pd.errors.EmptyDataError:
        sg.popup_error(f"O arquivo '{xlsx_file_path}' está vazio ou mal formatado.",
                       font=constantes.FONTE, title="Erro")
    except sqlite3.Error as e:
        sg.popup_error(f"Erro no banco de dados SQLite: {e}",
                       font=constantes.FONTE, title="Erro")
    except Exception as e:
        sg.popup_error(f"Ocorreu um erro inesperado: {e}",
                       font=constantes.FONTE, title="Erro")
