valores = []

while True:
    valores.append(int(input('Digite um valor : ')))
    cont = str(input('Digitar outro número ?[S/N] ')).upper().strip()
    if cont[0] != 'S' and cont[0] != 'N':
        while cont[0] != 'S' and cont[0] != 'N':
            cont = str(input('\033[31mOPÇÃO INVÁLIDA\033[m.Digitar outro número ?[S/N] ')).upper().strip()
    if cont[0] == 'N':
        break


par = []
impar = []
for c in valores:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)

print(f'A lista completa é {valores}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')