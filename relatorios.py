import PySimpleGUI as sg
import funcoes_registro

def somar_e_exibir_total_de_familias():
    conn = funcoes_registro.conectar_banco_de_dados()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(Num_Familias) FROM SISREQ")

    total_familias = cursor.fetchone()[0]

    if total_familias is not None:
        sg.popup(f'Total: {total_familias} Famílias em processos de regularização.', title='Total de Famílias')
    else:
        sg.popup('Não há registros para exibir.', title='Erro')

def somar_e_exibir_area_total():
    conn = funcoes_registro.conectar_banco_de_dados()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(Area_ha) FROM SISREQ")

    total_area = cursor.fetchone()[0]

    if total_area is not None:
        total_area_formatado = "{:.2f}".format(total_area)

        sg.popup(f'Área Total: {total_area_formatado} hectares em processos de regularização.', title='Total de Área')
    else:
        sg.popup('Não há registros para exibir.', title='Erro')