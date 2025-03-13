pessoas = []
dados = {}

while True:
    dados['nome'] = str(input('Nome: ').strip().capitalize())
    sexo = str(input('Sexo: [M/F] ')).strip().upper()
    while sexo[0] != 'M' and sexo != 'F':
        sexo = str(input('\033[31mOPÇÃO INVÁLIDA\033[m.Sexo: [M/F] ')).strip().upper()
    dados['sexo'] = sexo
    dados['idade'] = int(input('Idade: '))
    pessoas.append(dados.copy())
    dados.clear()
    cont = str(input('Quer continuar ? [S/N] ')).upper().strip()
    while cont[0] not in 'SN':
        cont = str(input('\033[31mOPÇÃO INVÁLIDA\033[m.Quer continuar ? [S/N] ')).strip().upper()
    if cont[0] == 'N':
        break
print(pessoas)