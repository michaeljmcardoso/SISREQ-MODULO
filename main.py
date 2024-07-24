import PySimpleGUI as sg
import funcoesRegistro
from aplicacao import Aplicacao

def main():
    conn = funcoesRegistro.conectar_banco_de_dados()
    if conn is not None:
        funcoesRegistro.criar_tabela_se_nao_existir(conn)
    app = Aplicacao()
    app.iniciar()
    
if __name__ == "__main__":
    main()