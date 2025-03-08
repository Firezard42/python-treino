print('='*45)
print('LISTAGEM DE PREÇO'.center(40))
print('='*45)
produtos = ('Lápis',1.75,'Borracha',2,'Caderno',15.90,'Estojo',25,'Transferidor',4.20,'Compasso',9.99,'Mochila',120.32,'Caneta',22.30,'Livro',34.90)

n1 = 0
n2 = 1
while True:
    print(f'{produtos[n1]:.<30}',f'R${produtos[n2]:.2f}')
    n1 += 2
    n2 += 2
    if n2 > len(produtos)-1:
        break