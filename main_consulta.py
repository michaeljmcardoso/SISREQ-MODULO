from licenca import check_license
from funcoes_registro import conectar_banco_de_dados, criar_tabela_se_nao_existir
from app_consulta import Aplicacao

def main():
    check_license()

    conn = conectar_banco_de_dados()
    if conn is not None:
        criar_tabela_se_nao_existir(conn)
        
    app = Aplicacao()
    app.iniciar()
    
if __name__ == "__main__":
    main()