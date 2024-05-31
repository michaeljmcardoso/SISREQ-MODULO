import PySimpleGUI as sg
import funcoes
from aplicacao import Aplicacao

def main():
    conn = funcoes.conectar_banco_de_dados()
    if conn is not None:
        funcoes.criar_tabela_se_nao_existir(conn)
    app = Aplicacao()
    app.iniciar()
    
if __name__ == "__main__":
    main()