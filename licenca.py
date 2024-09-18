import PySimpleGUI as sg
import constantes
import datetime
import sys

def check_license():
    today = datetime.datetime.now().date()

    expiration_date = datetime.datetime.strptime("2025-03-15", "%Y-%m-%d").date()  # prazo da licença

    if today > expiration_date:
        sg.popup_error("Licença expirada. Entre em contato para renovar:", "Whatsapp => (98) 98895-7452", "Email => michaeljmc@outlook.com.br", 
                    title="Aviso", 
                    font=constantes.FONTE_DE_AVSIO)
        
        sys.exit(1)
    
    if today == expiration_date:
        sg.popup("Sua licença expira hoje. Entre em contato para renovar:", "Whatsapp => (98) 98895-7452", "Email => michaeljmc@outlook.com.br", 
                title="Aviso", 
                font=constantes.FONTE_DE_AVSIO)
       
    else:
        None