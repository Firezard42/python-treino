aluno = dict()
aluno['nome'] = str(input('Nome : '))
aluno['média'] = float(input(f'Média de {aluno['nome']} : ').strip().capitalize())
if aluno['média'] >= 6:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'
for k,v in aluno.items():
    print(f'{k} é igual a {v}')