class MinhaClasse:

    estatico = 'lhama'

    def __init__(self,estado):
        self._estado = estado

obj = MinhaClasse(True)
obj2= MinhaClasse(True)

MinhaClasse.estatico = 'peixe'  #Vai mudar todos os 3 prints estatico  para frango
obj.estatico = 'frango' #muda apenas o print estatico do obj selecionado, mas também cria um espelho que dizer que mesmo que o Minhaclasse.estatico seja alterado, essa mudança do objeto.estatico que continua valendo
MinhaClasse.estatico = 'LhamaAqui'

print(MinhaClasse.estatico)
print(obj.estatico)
print(obj2.estatico)