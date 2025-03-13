pessoas = []
dados = []
maior = 0
menor = 0

while True:
    dados.append(str(input('Nome : ').strip().capitalize()))
    dados.append(float(input('Peso : ')))
    pessoas.append(dados[:])
    if dados[1] > maior:
        maior = dados[1]

    if dados[1] < menor or len(pessoas) == 1:
        menor = dados[1]

    cont = str(input('Quer continuar? [S/N] ')).upper().strip()
    while cont[0] != 'S' and cont[0] != 'N':
        cont = str(input('\033[31mOPÇÃO INVÁLIDA\033[m.Quer continuar? [S/N] ')).upper().strip()
    if cont[0] == 'N':
        break
    dados.clear()




print(f'Ao todo, você cadastrou {len(pessoas)} pessoas. ')
print(f'O Maior peso foi de {maior:.2f}Kg. Peso de ',end='')
for c in pessoas:
    if c[1] == maior:
       print('[',c[0],']',end=' ')

print('')
print(f'O Menor peso foi de {menor:.2f}Kg. Peso de ',end='')
for c in pessoas:
    if c[1] == menor:
        print('[',c[0],']',end=' ')