valores = []

while True:
    valores.append(int(input('Digite um número : ')))
    cont = str(input('Digitar outro número ? [S/N] ' )).upper().strip()
    if cont[0] != 'S' and cont[0] != 'N':
        while cont[0] != 'S' and cont[0] != 'N':
            cont = str(input('\033[31mOPÇÃO INCORRETA\033[m.Digitar outro número ? [S/N] ' )).upper().strip()
    if cont[0] == 'N':
        break

print(f'Total de números digitados : {len(valores)}')
valores.sort(reverse=True)
print(f'Lista de valores em forma decrescente : {valores}')
if 5 in valores:
    print('O Valor 5 está na lista.')
else:
    print('Não tem o valor 5 na lista.')


