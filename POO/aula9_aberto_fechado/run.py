class Artista:
    def __init__(self, tipo: str):
        self.tipo = tipo
    
    def apresenta_show(self):
        print(f'O {self.tipo} está apresentando o seu show')
    

class Circo:
    def apresentar(self,artista : Artista):
        artista.apresenta_show()


teste = Circo()

palhaço = Artista('palhaço')
magico = Artista('Mágico')

teste.apresentar(magico)
        