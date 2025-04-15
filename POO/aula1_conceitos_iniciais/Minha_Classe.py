class MinhaClasse:
    def __init__(self, info, pira): #metodo construtor que serve pra criar os atributos
         #print('Estou no método construtor') #esse método vai rodar antes de todos os codigos, no momento em que você instanciar o objeto, sem necessitar faer a ação pelo objeto.
        self.atributo1 = 'meu atributo'
        self.atributo2 = 123 #um atributo pode ser muitas coisas como listas,floats,numeros inteiros,strings e etc...
        self.atributo3 = [1,2,'a']
        self.new_atribute = info
        self.atributo_pira = pira
        print(self.new_atribute)

    #sempre lembre de colocar o self dentro dos métodos e dos atributos pra sinalizar que o def faz parte da classe.

    def metodo1(self):
        print('minha ação ')
        print(self.atributo_pira)
        return 'Hello World !!!'

    def metodo2(self,numero):
        self.metodo1() #você pode chamar um metodo dentro do outro, nesse caso isso vai fazer você mostrar o metodo1 mesmo so chamando o metodo2 quando o objeto for realizar a ação. 
        #e sempre lembre de usar o self. antes no metodo que vai chamar
        print(self.atributo3[1] + numero) 
        

#objeto         #classe -> instanciamos o objeto
minha_classe = MinhaClasse("info aqui no construtor","pira aqui man")

#quem vai realizar a ação é o objeto, como se fosse uma função
#response = minha_classe.metodo1()
#print(response)

minha_classe.metodo2(3)