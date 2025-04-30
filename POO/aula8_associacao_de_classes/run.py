class Interruptor:
    def __init__(self,comodo : str):
        self.comodo = comodo
    
    def acender(self):
        print(f'Estou acendendo a luz do comodo : {self.comodo}')

    def apagar(self):
        print(f'Estou apagando a luz do comodo : {self.comodo}')
    

class Pessoa:

    def acender_luzes(self, interruptor: Interruptor):
        interruptor.acender()
    
    def apagar_luzes(self, interruptor: Interruptor):
        interruptor.apagar()
    
    def dormir(self):
        print('A pessoa foi dormir')

jurisvaldo = Pessoa()
comodo_sala = Interruptor('Sala')
comodo_quarto = Interruptor('Quarto')

jurisvaldo.acender_luzes(comodo_sala)
jurisvaldo.apagar_luzes(comodo_quarto)
