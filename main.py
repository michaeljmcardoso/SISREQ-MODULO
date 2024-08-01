import PySimpleGUI as sg
import funcoes_banco_de_dados
from aplicacao import Aplicacao

def main():
    conn = funcoes_banco_de_dados.conectar_banco_de_dados()
    if conn is not None:
        funcoes_banco_de_dados.criar_tabela_se_nao_existir(conn)
    app = Aplicacao()
    app.iniciar()
    
if __name__ == "__main__":
    main()