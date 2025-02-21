d = float(input('Qual é a distância da viagem em Km ? '))
if d > 200:
    p = d * 0.45
    print(f'O Preço da passagem será R${p:.2f}')
else:
    p = d * 0.50
    print(f'O Preço da passagem será R${p:.2f}')