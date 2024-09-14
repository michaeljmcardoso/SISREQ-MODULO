import PySimpleGUI as sg
import datetime

"""Constantes de janela"""

ANO_ATUAL = datetime.datetime.now().year

JANELA_TEMA = sg.theme('DarkGreen')

JANELA_RODAPE = sg.Text(f"Desenvolvido por Michael JM Cardoso. © {ANO_ATUAL}\n             Todos os direitos reservados.", text_color='black', font='Helvetica 8 bold')

FONTE = font='Helvetica 10 bold'

FONTE_DE_AVSIO = font='Any 10 bold'

"""Constantes de listas"""

TIPO_SOBREPOSICAO = [
    'PA_INCRA', 
    'PA_ESTADUAL', 
    'AREA_PARTICULAR', 
    'OUTRO_TQ', 
    'TERRAS_DE_MARINHA', 
    'TERRAS_DEVOLUTAS', 
    'TERRAS_INDÍGENAS', 
    'TERRAS_DA_UNIÃO', 
    'SEM_SOBREPOSIÇÃO',  
    'SEM_INFORMAÇÃO'                      
    ]

ETAPA_RTID = [
    'Sem_RTID', 
    'RTID_Concluído', 
    'Antropológico_concluído', 
    'Antropológico_andamento', 
    'Cadastro_família_concluído', 
    'Cadastro_família_andamento', 
    'Fundiário_concluído',
    'Fundiário_andamento', 
    'Cartorial_concluído', 
    'Cartorial_andamento', 
    'Parecer_Técnico',
    'Parecer_Jurídico', 
    'CDR'
    ]

FASE_PROCESSO = [ 
    'Inicial', 
    'RTID',
    'Publicação', 
    'Notificação', 
    'Contestação', 
    'Recurso', 
    'Portaria',  
    'Decreto', 
    'Desapropriação', 
    'Titulação', 
    'Desintrusão'
    ]  

CERTIFICACAO_FCP = [
    'Certificada', 
    'Não-certificada'
    ]

ACAO_CIVIL_PUBLICA = [
    'Com_Sentença', 
    'Sem_Sentença', 
    'Com_Decisão_Liminar', 
    'Sentença_Cumprida', 
    'Sem_ACP', 
    'Corte_InterAmericana'
    ] 

RELATORIO_ANTROPOLOGICO = [
    'Execução_Direta',
    'Contrato',
    'Acordo_Coop_Técnica',
    'Doação',
    'Termo_Execução_Descentralizada',
    'Sem_Relatório'
    ]

PNRA = ['ANDAMENTO','CONCLUIDO','NAO-INICIADO']