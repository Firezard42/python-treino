pessoas = []
dados = {}
mulheres = []
media = 0

while True:
    dados['nome'] = str(input('Nome: ').strip().capitalize())
    sexo = str(input('Sexo: [M/F] ')).strip().upper()
    while sexo[0] != 'M' and sexo[0] != 'F':
        sexo = str(input('\033[31mOPÇÃO INVÁLIDA\033[m.Sexo: [M/F] ')).strip().upper()
    dados['sexo'] = sexo
    dados['idade'] = int(input('Idade: '))
    media = dados['idade']+media
    if sexo[0] == 'F':
        mulheres.append(dados['nome'][:])
    pessoas.append(dados.copy())
    dados.clear()
    cont = str(input('Quer continuar ? [S/N] ')).upper().strip()
    while cont[0] not in 'SN':
        cont = str(input('\033[31mOPÇÃO INVÁLIDA\033[m.Quer continuar ? [S/N] ')).strip().upper()
    if cont[0] == 'N':
        break
media = media/len(pessoas)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'Media de idade das pessoas cadastradas é {media:.2f}.')
print(f'Mulheres cadastradas são: ',end='')
for c in mulheres:
    if c == mulheres[len(mulheres)-1]:
        print(c)
    else:
        print(c,end=',')
print('Lista de pessoas acima da média:')
for c in pessoas:
    if c['idade'] > media:
        for k,v in c.items():
            print(f'{k} = {v};',end='  ')
        print('')
