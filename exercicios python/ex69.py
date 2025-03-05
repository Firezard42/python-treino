maiores = 0
mens = 0
girls = 0

while True:
    idade = int(input('Digite a idade do cliente : '))
    sexo = str(input('Digite o sexo do cliente [M/F] : ')).upper().strip()
    if sexo[0] != 'M' and sexo[0] != 'F':
        while sexo[0] != 'M' and sexo[0] != 'F':
            sexo = (str(input('\033[31mOPÇÃO INCORRETA\033[m, DIGITE "M" PARA MACHO OU "F" PARA FÊMEA : '))).upper().strip()

    if idade > 18:
        maiores += 1

    if sexo[0] == 'M':
        mens += 1

    if sexo[0] == 'F' and idade < 20:
        girls += 1

    cont = str(input('Cadastrar mais pessoas [S/N] ? ')).upper().strip()
    if cont[0] != 'S' and cont[0] != 'N':
        while cont[0] != 'S' and cont[0] != 'N':
            cont = str(input('\033[31mOPÇÃO INVÁLIDA.\033[m Cadastrar mais pessoas [S/N] ? ')).upper().strip()

    if cont[0] == 'N':
        print('FINALIZANDO PROGRAMA...')
        break

print(f'O TOTAL DE PESSOAS MAIORES DE 18 ANOS É : {maiores}')
print(f'O TOTAL DE HOMENS CADASTRADOS É : {mens}')
print(f'O TOTAL DE MULHERES COM MENOS DE 20 ANOS É : {girls}')



