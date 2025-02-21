v = float(input('Qual a velocidade que esse carro ai correu meu nobre ? '))
if v > 80:
    m = (v-80) * 7
    print(f'Então você correu {v:.1f}Km/h ?, está multadinho em R${m:.2f}')
else:
    print('Tudo certo meu patrão, pode ir embora.')