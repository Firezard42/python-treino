import datetime
ano = datetime.datetime.now().year
pessoa = {}
pessoa['nome'] = str(input('Nome : '))
pessoa['idade'] = ano - int(input('Ano de nascimento : '))
pessoa['ctps'] = int(input('Carteira de trabalho (digite 0 se não tiver): '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação : '))
    pessoa['Salário'] = float(input('Salário: R$ '))
    pessoa['aposentadoria'] = (pessoa['contratação'] + 35) - (ano - pessoa['idade'])

print('=-'*45)
print(pessoa)
for k,v in pessoa.items():
    print(f'{k} tem o valor {v}')