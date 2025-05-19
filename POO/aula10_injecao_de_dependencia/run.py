class Celular:
    
    def __init__(self,modelo = str):
        self.modelo = modelo
    
    def enviar_mensagem(self,mensagem = str):
        print(f'Mensagem enviada: {mensagem}')

    def abrir_emails(self):
        print('ABRINDO EMAILS...')
    
    def abrir_youtube(self):
        print('ABRINDO YOUTUBE...')

class Pessoa:
    def __init__(self, celular : Celular):
        self._celular = celular
    
    def pedir_pizza(self):
        print('Abrindo o Zap')
        self._celular.enviar_mensagem('Pizza de Calabresa')
    
    def estudar(self):
         self._celular.abrir_youtube()
         print('Anotando conteúdo')


android = Celular('Samsung')
apple = Celular('Iphone')
jose = Pessoa(android)

jose.pedir_pizza()

jose.estudar()