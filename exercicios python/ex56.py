media = 0
cont  = 0
velho = ''
velho2= 0

for c in range(1,5):
    nome = str(input(f'Qual é o nome da {c}ª pessoa : ')).strip().title()
    idade = int(input(f'Qual é a idade da {c}ª pessoa : '))
    sexo = str(input(f'Qual é o sexo da {c}ª pessoa ? [M/F]')).strip().upper()
    media += idade
    if sexo[0] == 'F' and idade < 20:
        cont += 1
    if idade > velho2 and sexo[0] == 'M':
        velho2 = idade
        velho = nome


print(f'A idade média dessas pessoas é {media/4:.0f} anos')
if cont == 1:
    print(f'{cont} mulher tem menos de 20 anos')
else:
    print(f'{cont} mulheres tem menos de 20 anos')

if velho2 == 0:
    print('Não existe homens no local')
else:
    print(f'o homem mais velho é o {velho}, com {velho2} anos')
