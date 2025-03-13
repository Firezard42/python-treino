alunos = []
alunos2 = []
media = 0
while True:
    alunos2.append(str(input('Nome : ').strip().capitalize()))
    alunos2.append(float(input('Nota 1 : ')))
    alunos2.append(float(input('Nota 2 : ')))
    media = (alunos2[1]+alunos2[2])/2
    alunos2.append(media)
    alunos.append(alunos2[:])
    alunos2.clear()
    cont = str(input('Quer Continuar ? [S/N] ')).strip().upper()
    while cont[0] not in 'SN':
        cont = str(input('Quer Continuar ? [S/N] ')).strip().upper()
    if cont[0] == 'N':
        break

print('=-'*30)
print(f'No.  NOME          {'MÉDIA':^10}')
print('-'*35)
for e,c in enumerate(alunos):
    print(f'{e}   {c[0]:<10}      {c[3]:>5.1f}')
print('=-'*30)
while True:
    notas = int(input('Digite o No. do aluno que você deseja vê as notas (999 para interromper) : '))
    if notas == 999:
        break
    if notas < len(alunos) and notas >= 0:
        for e,c in enumerate(alunos):
            if e == notas:
                print(f'As notas de {c[0]} são {c[1]} e {c[2]} ')
    else:
        print(f'\033[31mNúmero inválido\033[m, tente digitar entre 0 - {len(alunos)-1} ')
print('FINALIZANDO...')