import PySimpleGUI as sg
import funcoes

def construir_janela():
    layout = [[sg.Text("Olá, mundo!")], 
              [sg.Button("OK")]]
    janela = sg.Window("Sistema de Regularização Quilombola (v.0.01)", layout)
    return janela

def main():
    conn = funcoes.conectar_banco_de_dados()
    if conn is not None:
        funcoes.criar_tabela_se_nao_existir(conn)
    janela_principal = construir_janela()

    while True:
        event, values = janela_principal.read()
        if event == "OK" or event == sg.WIN_CLOSED:
            break

    janela_principal.close()
    conn.close()

if __name__ == "__main__":
    main()
