import funcoes_registro
from aplicacao import Aplicacao
from aplicacao import check_license

def main():
    check_license()

    conn = funcoes_registro.conectar_banco_de_dados()
    if conn is not None:
        funcoes_registro.criar_tabela_se_nao_existir(conn)
        
    app = Aplicacao()
    app.iniciar()
    
if __name__ == "__main__":
    main()