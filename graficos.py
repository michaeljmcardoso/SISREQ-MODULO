import PySimpleGUI as sg
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import webbrowser
from constantes import FONTE
from funcoes_registro import conectar_banco_de_dados

plt.switch_backend('TkAgg') # Backend específico para exibir gráficos

"""Funções para criar visualizações gráficas"""

def exibir_processos_por_municipio():
    conn = conectar_banco_de_dados ()
    cursor = conn.cursor()

    cursor.execute("SELECT Municipio, COUNT(*) AS Num_Processos FROM SISREQ GROUP BY Municipio")
    resultados = cursor.fetchall()

    if resultados:
        municipios = []
        num_processos = []

        for resultado in resultados:
            municipios.append(resultado[0])
            num_processos.append(resultado[1])

        # Criar DataFrame
        data = pd.DataFrame({'Municípios': municipios, 'Número de Processos': num_processos})

        # Plot do gráfico
        fig, ax = plt.subplots(figsize=(10, 6))
        num_cores = len(municipios)
        palette = sns.color_palette("viridis", num_cores)
        sns.barplot(x=num_processos, y=municipios, data=data, palette=palette)

        # Configurações do gráfico
        ax.set(title='Número de Processos por Município')  # Título
        sns.set_style("white")
        sns.despine(right=True, top=True, bottom=True, left=True)
        plt.tick_params(bottom=False, labelbottom=False)

        # Adicionar rótulos (quantidades) ao lado de cada barra
        for i, num_processos in enumerate(num_processos):
            ax.text(num_processos + 0.1, i, str(num_processos), ha='left', va='center', weight='bold', fontsize='8')

        plt.tight_layout()
        plt.show()
    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=FONTE)


def exibir_processos_por_data_abertura():
    conn = conectar_banco_de_dados()
    cursor = conn.cursor()

    cursor.execute("SELECT Data_Abertura, COUNT(*) AS Num_Processos FROM SISREQ GROUP BY Data_Abertura")
    resultados = cursor.fetchall()

    if resultados:
        datas_abertura = []
        num_processos = []

        for resultado in resultados:
            datas_abertura.append(resultado[0])
            num_processos.append(resultado[1])

        # Criar DataFrame
        data = pd.DataFrame({'Data de Abertura': datas_abertura, 'Número de Processos': num_processos})

        # Converter a coluna de datas para o formato apropriado (opcional)
        data['Data de Abertura'] = pd.to_datetime(data['Data de Abertura'], format="%d-%m-%Y")

        # Ordenar o DataFrame por data de abertura
        data = data.sort_values(by='Data de Abertura')

        # Calcular o acumulado de processos por ano
        data['Ano'] = data['Data de Abertura'].dt.year
        acumulado_por_ano = data.groupby('Ano')['Número de Processos'].cumsum()

        # Adicionar a coluna de acumulado de processos ao DataFrame
        data['Acumulado'] = acumulado_por_ano

        # Plot do gráfico de linhas
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.lineplot(x='Data de Abertura', y='Acumulado', data=data, palette="Set1")

        # Configurações do gráfico
        ax.set(title='Acumulado de Processos por Ano')
        ax.set_xlabel('Ano de Abertura')
        sns.set_style("white")
        sns.despine(right=True, top=True, bottom=False, left=False)
        plt.xticks(rotation=45)  # Rotacionar os rótulos do eixo x para melhor legibilidade

        plt.tight_layout()
        plt.show()
    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=FONTE)


def exibir_processos_com_acao_civil():
    conn = conectar_banco_de_dados()
    cursor = conn.cursor()

    cursor.execute("SELECT Acao_Civil_Publica, COUNT(*) AS Tipo_AcaoCivilPublica FROM SISREQ WHERE Acao_Civil_Publica != 'Sem_ACP' GROUP BY Acao_Civil_Publica")
    resultados = cursor.fetchall()

    if resultados:
        acaocivil = []
        tipo_decisao = []

        for resultado in resultados:
            acaocivil.append(resultado[0])
            tipo_decisao.append(resultado[1])

        # Criar DataFrame
        data = pd.DataFrame({'ACP': acaocivil, 'Tipo de ACP': tipo_decisao})
        # data = data.sort_values(by='Acao_Civil_Publica', ascending=False)

        # Plot do gráfico
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x=tipo_decisao, y=acaocivil, data=data, palette="Set1")

        # Configurações do gráfico
        ax.set(title='Ação Civil Pública em Regularização Quilombola')  # Título
        sns.set_style("white")
        sns.despine(right=True, top=True, bottom=True, left=True)
        plt.tick_params(bottom=False, labelbottom=False)

        # Adicionar rótulos (quantidades) em cima de cada barra
        for i, tipo_decisao in enumerate(tipo_decisao):
            ax.text(tipo_decisao + 0.1, i, str(tipo_decisao), ha='left', va='center', weight='bold')

        plt.tight_layout()
        plt.show()
    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=FONTE)


def exibir_processos_por_fase_atual():
    conn = conectar_banco_de_dados()
    cursor = conn.cursor()

    cursor.execute("SELECT Fase_Processo, COUNT(*) as Total FROM SISREQ WHERE Fase_Processo != 'Inicial' GROUP BY Fase_Processo")
    registros = cursor.fetchall()

    if registros:
        # Extrair os dados das fases e suas contagens
        fases = [registro[0] for registro in registros]
        contagens = [registro[1] for registro in registros]

        # criar um DataFrame
        data = pd.DataFrame({'Fase': fases, 'Contagem': contagens})

        # Criar o gráfico de barras
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x=contagens, y=fases, data=data, palette="Set1")

        # Configurações do gráfico
        ax.set(title='Processos por Fase')
        sns.despine(right=True, top=True, bottom=True, left=True)
        plt.tick_params(bottom=False, labelbottom=False)

        # Adicionar rótulos (quantidades) ao lado de cada barra
        for i, contagens in enumerate(contagens):
            ax.text(contagens + 0.1, i, str(contagens), ha='left', va='center', weight='bold', fontsize='10')

        plt.tight_layout()
        plt.show()
    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=FONTE)


def exibir_andamento_de_processos():
    conn = conectar_banco_de_dados()
    cursor = conn.cursor()

    cursor.execute("SELECT CASE WHEN Fase_Processo = 'Inicial' THEN 'Inicial' ELSE 'Andamento' END AS Fase, COUNT(*) as Total FROM SISREQ GROUP BY Fase")
    registros = cursor.fetchall()

    if registros:
        # Extrair os dados das fases e suas contagens
        fases = [registro[0] for registro in registros]
        contagens = [registro[1] for registro in registros]

        # Criar o DataFrame
        data = pd.DataFrame({'Fase': fases, 'Contagem': contagens})

        # Criar o gráfico de barras
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x=contagens, y=fases, data=data, palette="Set1")

        # Configurações do gráfico
        ax.set(title='Andamento de Processos')

        sns.despine(right=True, top=True, bottom=True, left=True)
        plt.tick_params(bottom=False, labelbottom=False)

        # Adicionar rótulos (quantidades) ao lado de cada barra
        for i, contagem in enumerate(contagens):
            ax.text(contagem + 0.1, i, str(contagem), ha='left', va='center', weight='bold', fontsize='10')

        plt.tight_layout()
        plt.show()

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=FONTE)


def exibir_tipo_de_sopreposicao():
    conn = conectar_banco_de_dados()
    cursor = conn.cursor()

    cursor.execute("SELECT Sobreposicao, COUNT(*) AS Tipo_Sobreposicao FROM SISREQ GROUP BY Sobreposicao")
    resultados = cursor.fetchall()

    if resultados:
        sobreposicao = []
        tipo_de_sobreposicao = []

        for resultado in resultados:
            if 'SEM_INFORMAÇÃO' not in resultado [0]: # Verifica se 'SEM_INFORMAÇÃO' não está presente na lista
                sobreposicao.append(resultado[0])
                tipo_de_sobreposicao.append(resultado[1])

        # Criar DataFrame
        data = pd.DataFrame({'Sobreposição': sobreposicao, 'Tipo de Sobreposição': tipo_de_sobreposicao})
        # data = data.sort_values(by='Sobreposicao', ascending=False)

        # Plot do gráfico
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x=tipo_de_sobreposicao, y=sobreposicao, data=data, palette='Set1')

        # Configurações do gráfico
        ax.set(title='Tipos de Sobreposição')  # Título
        sns.set_style("white")
        sns.despine(right=True, top=True, bottom=True, left=True)
        plt.tick_params(bottom=False, labelbottom=False)

        # Adicionar rótulos (quantidades) ao lado de cada barra
        for i, tipo_de_sobreposicao in enumerate(tipo_de_sobreposicao):
            ax.text(tipo_de_sobreposicao + 0.1, i, str(tipo_de_sobreposicao), ha='left', va='center', weight='bold')

        plt.tight_layout()
        plt.show()
    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=FONTE)


def exibir_relatorios_antropologicos_por_forma_de_elaboracao():
    conn = conectar_banco_de_dados()
    cursor = conn.cursor()

    cursor.execute("SELECT Relatorio_Antropologico, COUNT(*) AS Rel_Antropologico FROM SISREQ WHERE Relatorio_Antropologico != 'Sem_Relatório' GROUP BY Relatorio_Antropologico")
    resultados = cursor.fetchall()

    if resultados:
        relatorios = []
        tipo_relatorios = []

        for resultado in resultados:
            relatorios.append(resultado[0])
            tipo_relatorios.append(resultado[1])

        # Criar DataFrame
        data = pd.DataFrame({'Relatórios': relatorios, 'Tipo de Relatórios': tipo_relatorios})

        # Plot do gráfico sem o uso de palette
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x=tipo_relatorios, y=relatorios, data=data, palette='Set1')

        # Configurações do gráfico
        ax.set(title='Relatórios Antropológicos por Forma de Execução')  # Título
        sns.set_style("white")
        sns.despine(right=True, top=True, bottom=True, left=True)
        plt.tick_params(bottom=False, labelbottom=False)

        # Adicionar rótulos (quantidades) ao lado de cada barra
        for i, valor in enumerate(tipo_relatorios):
            ax.text(valor + 0.1, i, str(valor), ha='left', va='center', weight='bold')

        plt.tight_layout()
        plt.show()

    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=FONTE)


def plotar_mapa_interativo():
    conn = conectar_banco_de_dados()
    cursor = conn.cursor()

    cursor.execute("SELECT Municipio, Comunidade, Latitude, Longitude, Num_Familias FROM SISREQ")
    resultados = cursor.fetchall()

    if resultados:
        municipios = []
        comunidades = []
        latitudes = []
        longitudes = []
        numero_de_familias = []

        for resultados in resultados:
            municipios.append(resultados[0])
            comunidades.append(resultados[1])

            # Verificar se os valores de latitude e longitude são numéricos antes de adicioná-los
            if isinstance(resultados[2], (float, int)) and isinstance(resultados[3], (float, int)):
                latitudes.append(resultados[2])
                longitudes.append(resultados[3])
            else:
                latitudes.append(None)  # Se não for numérico, adicione None
                longitudes.append(None)

            numero_de_familias.append(resultados[4])

        df = pd.DataFrame({'Municipio': municipios, 'Comunidade': comunidades, 'Latitude': latitudes, 'Longitude': longitudes, 'Num_Familias': numero_de_familias})

        # Filtrar linhas com valores não nulos nas colunas de latitude e longitude
        df = df.dropna(subset=['Latitude', 'Longitude'])

        if not df.empty:
            px.set_mapbox_access_token('pk.eyJ1IjoibWpkYXRhc2NpZW5jZSIsImEiOiJjbGFlY3hwbGcwbWlxM3Nxa2NuOWh4cmNzIn0.2ye_ghCe_WAgIpqueUqedA')

            fig = px.scatter_mapbox(
                df, 
                lat='Latitude', 
                lon='Longitude',
                color=df['Municipio'],
                color_discrete_sequence=["fuchsia"],
                size_max=15,
                zoom=10,
                hover_name='Comunidade',
                hover_data='Num_Familias',
                height=700,
            )

            fig.update_layout(mapbox_style="streets")
            fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
            fig.write_html('mapa_interativo.html')

            webbrowser.open('mapa_interativo.html')

        else:
            sg.popup('Não há registros válidos para exibir.', title='Erro', font=FONTE)
    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=FONTE)


def exibir_status_pnra():
    conn = conectar_banco_de_dados()
    cursor = conn.cursor()

    # Consulta ao banco de dados para contar os status de PNRA
    cursor.execute("""
        SELECT PNRA, COUNT(*) AS Tipo_PNRA 
        FROM SISREQ 
        WHERE PNRA IN ('ANDAMENTO', 'CONCLUIDO', 'NAO-INICIADO') 
        GROUP BY PNRA
    """)
    resultados = cursor.fetchall()

    if resultados:
        pnra_status = []
        tipo_pnra = []

        for resultado in resultados:
            pnra_status.append(resultado[0])
            tipo_pnra.append(resultado[1])

        # Criar DataFrame com os dados de PNRA
        data = pd.DataFrame({'Status PNRA': pnra_status, 'Quantidade': tipo_pnra})

        # Plot do gráfico de barras
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x=tipo_pnra, y=pnra_status, data=data, palette="Set1", ax=ax)

        # Configurações do gráfico
        ax.set(title='Status do PNRA em Regularização Quilombola')  # Título
        sns.set_style("white")
        sns.despine(right=True, top=True, bottom=True, left=True)
        plt.tick_params(bottom=False, labelbottom=False)

        # Adicionar rótulos (quantidades) ao lado de cada barra
        for i, quantidade in enumerate(tipo_pnra):
            ax.text(quantidade + 0.0, i, str(quantidade), ha='left', va='center', weight='bold')

        plt.tight_layout()
        plt.show()
    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=FONTE)