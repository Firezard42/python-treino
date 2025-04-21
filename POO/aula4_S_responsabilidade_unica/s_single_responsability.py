#utilizando o principio de responsabilidade única
class SistemaCadastral:

    def cadastrar(self,nome: str,idade: int) -> None: #None significa que não vai retornar nada, apenas executar ações
        if self.__valid_input(nome,idade):
            self.__register_user(nome,idade)

        else:
            self.__erro_handle()


    def __valid_input(self,nome: str,idade : int) -> bool: #válida se nome é uma str e idade é um int
        return isinstance(nome,str) and isinstance(idade,int) #isinstance é usado pra verificar o tipo de objeto e retornar o booleano True ou False

    def __register_user(self,nome: str,idade: int)  -> None: #simula o processo de registro de um usuário
        print('Acessando o banco de dados...')
        print(f'Cadastrar usuario {nome}, idade {idade}')

    def __erro_handle(self) -> None: #mensagem de erro caso a validação de False
        print('Dados inválidos')

sistema = SistemaCadastral()
sistema.cadastrar('mario',28)