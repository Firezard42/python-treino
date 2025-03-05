tot = 0
mil = 0
cont2 = 0
barato = ''
barato2 = 0

while True:
    p1 = str(input('Digite o nome do produto : '))
    p2 = float(input('Qual é o preço do produto : '))
    tot = tot+p2
    if p2 > 1000:
        mil += 1

    if cont2 == 0:
        barato = p1
        barato2 = p2

    if p2 < barato2:
        barato = p1
        barato2 = p2

    cont2 += 1

    cont = str(input('Continuar passando produtos [S/N] ? ')).upper().strip()
    if cont and cont[0] not in 'SN':
        while cont[0] !='S' and cont[0] != 'N':
            cont = str(input('\033[31mOPÇÃO INVÁLIDA!!!.\033[mContinuar passando produtos [S/N] ? ')).upper().strip()

    if cont[0] == 'N':
        break


print(f'Total gasto foi : R${tot:.2f}')
print(f'{mil} Produtos custaram mais de R$1000')
print(f'O produto mais barato foi o {barato} que custou R${barato2:.2f}')

