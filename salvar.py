import PySimpleGUI as sg
from funcoes_registro import conectar_banco_de_dados
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import constantes

"""Funções para salvar planilhas"""

def salvar_planilha(registros):
    conn = conectar_banco_de_dados()
    if conn is not None:
        cursor = conn.cursor()

    cursor.execute("SELECT * FROM SISREQ")
    registros = cursor.fetchall()
    if registros:
        df = pd.DataFrame(
            registros,     
            columns=[
                'ID', 
                'Numero', 
                'Data_Abertura',
                'Comunidade',
                'Municipio',
                'Area_ha',
                'Num_familias',
                'Fase_Processo',
                'Etapa_RTID',
                'Edital_DOU',
                'Edital_DOE',
                'Portaria_DOU',
                'Decreto_DOU',
                'Area_ha_Titulada',
                'PNRA',
                'Relatorio_Antropologico',
                'Latitude',
                'Longitude',
                'Certidao_FCP',
                'Data_Certificacao',
                'Sobreposicao',
                'Analise_de_Sobreposicao',
                'Acao_Civil_Publica',
                'Data_Decisao',
                'Teor_Decisao_Prazo_Sentença',
                'Outras_Informacoes'
                ]
            )
        
        # Abre uma janela para selecionar o local e o nome do arquivo
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
        root.destroy()  # Fecha a janela de seleção de arquivo

        if file_path:
            df.to_excel(file_path, index=False)
            sg.popup('Planilha extraída com sucesso!', title='Sucesso', font=constantes.FONTE)
        else:
            sg.popup('Nenhum arquivo selecionado. A planilha não foi salva.', title='Aviso', font=constantes.FONTE)
    else:
        sg.popup('Não há registros para extrair.', title='Erro', font=constantes.FONTE)


def salvar_extrato_planilha(registros):
    if registros:
        df = pd.DataFrame(
            registros,     
            columns=[
                'ID', 
                'Numero', 
                'Data_Abertura',
                'Comunidade',
                'Municipio',
                'Area_ha',
                'Num_familias',
                'Fase_Processo',
                'Etapa_RTID',
                'Edital_DOU',
                'Edital_DOE',
                'Portaria_DOU',
                'Decreto_DOU',
                'Area_ha_Titulada',
                'PNRA',
                'Relatorio_Antropologico',
                'Latitude',
                'Longitude',
                'Certidao_FCP',
                'Data_Certificacao',
                'Sobreposicao',
                'Analise_de_Sobreposicao',
                'Acao_Civil_Publica',
                'Data_Decisao',
                'Teor_Decisao_Prazo_Sentença',
                'Outras_Informacoes'
                ]
            )
        
        # Abre uma janela para selecionar o local e o nome do arquivo
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
        root.destroy()  # Fecha a janela de seleção de arquivo

        if file_path:
            df.to_excel(file_path, index=False)
            sg.popup('Planilha extraída com sucesso!', title='Sucesso', font=constantes.FONTE)
        else:
            sg.popup('Nenhum arquivo selecionado. O extrato não foi salvo.', title='Aviso', font=constantes.FONTE)
    else:
        sg.popup('Não há registros para extrair.', title='Erro', font=constantes.FONTE)