def area(l,c):
    area = l * c
    print(f'A área do seu terreno de {l}x{c} é de {area:.1f}m².')


l1 = float(input('LARGURA (m): '))
c1 = float(input('COMPRIMENTO (m): '))
area(l1,c1)