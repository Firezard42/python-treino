n1 = int(input('Digite um número inteiro : '))
cont = 0

for c in range(1,n1+1):
    if n1 % c == 0:
        cont = cont+1

if cont == 2:
    print(f'\033[0;32m{n1} é um número primo\033[m')

else:
    print(f'\033[31m{n1} não é um número primo\033[m')