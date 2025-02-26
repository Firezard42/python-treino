import datetime
nasc = int(input('Qual é a data de nascimento do atleta ? '))
ano = datetime.datetime.now().year
idade = ano - nasc

if idade <= 9:
    print(f'Com {idade} anos, o atleta é de catégoria Mirim')

elif idade > 9 and idade <= 14:
    print(f'Com {idade} anos, o atleta é de catégoria Infantil')

elif idade > 14 and idade <= 19:
    print(f'Com {idade} anos, o atleta é de catégoria Junior')

elif idade > 19 and idade <= 25:
    print(f'Com {idade} anos, o atleta é de catégoria Sênior')

else:
    print(f'Com {idade} anos, o atleta é de catégoria Master')