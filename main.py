import funcoes_registro
import licenca
from aplicacao import Aplicacao


def main():
    licenca.check_license()

    conn = funcoes_registro.conectar_banco_de_dados()
    if conn is not None:
        funcoes_registro.criar_tabela_se_nao_existir(conn)
        
    app = Aplicacao()
    app.iniciar()
    
if __name__ == "__main__":
    main()