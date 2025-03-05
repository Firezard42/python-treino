p = 'SIM'
cont = 0
maior = 0
menor = 0
media = 0

while p[0] != 'N':
    n1 = int(input('Digite um número inteiro : '))
    if cont == 0:
        maior = n1
        menor = n1
    p = str(input('Digita outro Número ? [S/N] ')).strip().upper()
    while p != 'S' and p != 'N':
        p = str(input('\033[31mOPÇÃO INCORRETA\033[m, DIGITE "S" PARA SIM OU "N" PARA NÃO : ')).strip().upper()

    if n1 > maior:
        maior = n1
    if n1 < menor:
        menor = n1

    cont += 1
    media = media+n1

print(f'você digitou {cont} números e a média entre eles é {media/cont}')
print(f'O Maior número é o {maior}\nO Menor número é o {menor}')


