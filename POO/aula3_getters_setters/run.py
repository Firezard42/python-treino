class MinhaClasse:
    def __init__(self):
        self.__teste = None

    
    def setter(self,valor = int) -> None:
        self.__teste = valor
    
    def getter(self) -> int:
        return self.__teste
    


myclass = MinhaClasse()
myclass.setter(42)
valor = myclass.getter()
print(valor)