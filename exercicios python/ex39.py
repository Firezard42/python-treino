import datetime
nasc = int(input('Digite sua data de nascimento : '))
ano = datetime.datetime.now().year
idade = ano-nasc

if idade < 18:
    tempo = 18 - idade
    if tempo > 1:
        print(f'Ainda falta {tempo} anos para você se alistar')
    else:
        print(f'Ainda falta {tempo} ano para você se alistar')

elif idade == 18:
    print('JÁ FEZ 18 ANOS PAINHO, HORA DE CAPINARRRRR')

elif idade > 18:
    tempo = idade - 18
    if tempo > 1:
        print(f'meu amigo, você deveria ter se alistado a {tempo} anos')
    else:
        print(f'meu amigo, você deveria ter se alistado a {tempo} ano')