from UtilidadesCeV import moeda

n = float(input('Qual é o preço: R$'))
moeda.resumo(n,10,13)

print(f'O Dobro de {moeda.moeda(n)} é {moeda.dobro(n,True)}')
print(f'A Metade de {moeda.moeda(n)} é {moeda.metade(n,True)}')
print(f'Aumento de 10% é {moeda.aumentar(n,10,True)}')
print(f'Redução de 13% é {moeda.diminuir(n,13,True)}')