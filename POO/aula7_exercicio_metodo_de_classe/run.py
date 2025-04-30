class Loja:

    taxa = 1.15

    def __init__(self,valor : float):
        self.valor_produto_bruto = valor


    def consultar_valor_do_produto(self):
        valor_produto = self.valor_produto_bruto * self.taxa
        print(f'\033[32mO valor final do produto é: {valor_produto:.2f}\033[m')
    
    @classmethod
    def editar_taxa_do_produto(cls,taxa2: float):
        cls.taxa = taxa2 


loja_praia = Loja(29.90)
loja_shopping = Loja(20.22)

print('Antes de editar a taxa : ')
loja_shopping.consultar_valor_do_produto()
loja_praia.consultar_valor_do_produto()
print('-'*20)
loja_praia.editar_taxa_do_produto(2)
print('Depois de editar a taxa : ')
loja_shopping.consultar_valor_do_produto()
loja_praia.consultar_valor_do_produto()