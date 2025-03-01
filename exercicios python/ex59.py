n1 = float(input('Digite o primeiro valor : '))
n2 = float(input('Digite o segundo valor : '))
menu = 0
while menu != 5:
    menu = int(input('[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS NÚMEROS\n[5]SAIR DO PROGRAMA\n\033[33mDigite :\033[m '))
    if menu == 1:
        print('=-' * 12)
        print(f'{n1 + n2}')
        print('=-' * 12)
    elif menu == 2:
        print(f'{n1*n2}')
    elif menu == 3:
        maior = max(n1,n2)
        print('=-' * 12)
        print(maior)
        print('=-' * 12)
    elif menu == 4:
        print('=-' * 12)
        n1 = float(input('Digite o primeiro valor : '))
        n2 = float(input('Digite o segundo valor : '))
        print('=-' * 12)
    elif menu == 5:
        print('=-' * 12)
        print('ENCERRANDO PROGRAMA...')
        print('=-' * 12)

    else:
        print('=-'*12)
        print('\033[31mOPÇÃO INVÁLIDA\033[m')
        print('=-' * 12)