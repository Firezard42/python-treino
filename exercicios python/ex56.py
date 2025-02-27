media = 0
cont  = 0
velho = ''

for c in range(1,5):
    nome = str(input(f'Qual é o nome da {c}ª pessoa : ')).strip().title()
    idade = int(input(f'Qual é a idade da {c}ª pessoa : '))
    sexo = str(input(f'Qual é o sexo da {c}ª pessoa ? [M/F]')).strip().upper()
    if sexo[0] != 'M' and sexo[0] != 'F':
        print('\033[31mOPÇÃO INVÁLIDA\033[m')
    media += idade


print(f'{media/4}')
