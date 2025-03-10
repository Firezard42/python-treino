valores = []
while True:
    while True:
        valor = int(input('Digite um valor : '))
        if valor in valores:
            print('Valor duplicado! Não vou adicionar')
        else:
            valores.append(valor)
            break
    cont = str(input('Quer continuar ? [S/N] ')).strip().upper()
    if cont[0] != 'S' and cont[0] != 'N':
        while cont != 'S' and cont != 'N':
            cont = str(input('\033[31mOPÇÃO INVÁLIDA\033[m.Quer continuar ? [S/N] ')).upper().strip()
    if cont[0] == 'N':
        break


valores.sort()
print(f'Você digitou os valores {valores}')