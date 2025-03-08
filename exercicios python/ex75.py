n1 = int(input('Digite o primeiro valor : '))
n2 = int(input('Digite o segundo valor : '))
n3 = int(input('Digite o terceiro valor : '))
n4 = int(input('Digite o quarto valor : '))
tres = 0
cont = 0
valor = (n1,n2,n3,n4)
for c in valor:
    if c % 2 == 0:
        cont += 1
    if c == 3:
        tres = (valor.index(3))
print('O Nove apareceu : ',valor.count(9),' Vezes')
print(f'Os Valores pares digitados foram {cont}')
if tres == 3:
    print(f'O Número três apareceu pela primeira vez na {tres + 1}ªPosição.')
else:
    print(f'O Número três não foi digitado')
