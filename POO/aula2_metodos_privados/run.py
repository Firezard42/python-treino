class pessoa:
    def __init__(self,altura,cpf):
        self.__altura = altura
        self.cpf = cpf
    
    def apresentar(self):
        print(f'Minha altura é {self.__altura}')
        self.__coletar_documento()
    
    def __coletar_documento(self):
        print(f'Meu documento é {self.cpf}')

jorge = pessoa('1.73','000.111.222-33')


#jorge.__coletar_documento() #não vai funcionar, pois um metodo com __ antes do nome é considerado um método privado e método privados só podem ser acionados dentro da propria classe
#jorge.apresentar() #aqui o __coleter_documentos vai funcionar, pois ele vai ser acionado dentro do apresentar.

#print(jorge.__altura) #atributos também podem ser privados, assim você não consegue aciona-los fora da classe
#print(jorge.altura) #se a altura não fosse privado você conseguiria printar ela na tela com esse comando

#jorge.__altura = '123' 
#print(jorge.__altura)
# o codigo vai apresentar dois __altura diferentes, uma que você declarou no escopo de fora da classe e outra de dentro
#jorge.apresentar()