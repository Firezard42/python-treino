class ConectarBancodeDados:
    def __init__(self):
        self.conection = None
    
    def conectar_ao_banco(self):
        self.conection = True

class RepositorioBanco:
    def __init__(self, conexao: ConectarBancodeDados):
        self.__conexao = conexao
    
    def BuscarDados(self):
        if self.__conexao.conection:
            return [1,2,3,4,5]
        else:
            None
    

class RegraDeNegocio:
    def __init__(self, repo: RepositorioBanco):
        self._repo = repo
    
    def calcular_resultado(self):
        dados = self._repo.BuscarDados()
        if not  dados:
            print('Dados não encontrados')
        else:
            resposta = 0
            for c in dados:
                resposta = resposta + c
        print(f'O Resultado é {resposta}')

conn = ConectarBancodeDados()
conn.conectar_ao_banco()

repo = RepositorioBanco(conn)
regra = RegraDeNegocio(repo)

regra.calcular_resultado()