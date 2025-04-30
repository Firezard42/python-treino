class MinhaClasse:

    estatico = 'lhama'

    def __init__(self,estado):
        self._estado = estado

    
    def print_variavel_de_classe(self):
        print(self.estatico)

    #def alteracao_de_variavel_de_classe(self):
        #self.estatico = 'batata' -----------------#com esse método você apenas vai criar um espelho do estatico pra o objeto que acionar, ou seja vai causar alteração no objeto que acionar, mas nos demais ou se alguem acionar o print(MinhaClasse.estatico) ainda vai continuar 'lhama'---------

    @classmethod
    def alteracao_de_variavel_de_classe(cls):
        cls.estatico = 'batata' # usando  @classmethod e cls invés de self, se você usar obj.alteracao_de_variavel_de_classe() vai alterar todos os objetos pra 'batata' e a print(MinhaClasse.estatico) também.

obj = MinhaClasse(True)
obj2= MinhaClasse(True)

obj.print_variavel_de_classe()
obj.alteracao_de_variavel_de_classe()


print(obj.estatico)
print(obj2.estatico)
print(MinhaClasse.estatico)