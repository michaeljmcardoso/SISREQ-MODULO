import pysimplegui as sg

def construir_janela():
  layout = [[sg.Text("Olá, mundo!"], 
            [sg.Button("OK"]]
  return sg.Window("Sistema de Regularização Quilombola (v.0.01)", layout)
