from random import randint
print('='*12,'BEM VINDO AO IMPAR OU PAR GAME','='*12)
cont = 0

while True:
    n1 = int(input('Escolha um número : '))
    n2 = str(input('Par ou Ímpar? [P/I] : ')).upper().strip()
    if n2[0] != 'P' and n2[0] != 'I':
        while n2[0] != 'P' and n2[0] != 'I':
            print('\033[31mOPÇÃO INVÁLIDA\033[m')
            n2 = str(input('Par ou Ímpar? [P/I] : ')).upper().strip()

    cont += 1
    pc = randint(0,10)
    if (n1+pc) % 2 == 0 and n2[0] == 'P':
        print(f'Eu escolhi o número {pc} e você {n1}.Total deu {n1 + pc} PAR \033[32mVOCÊ VENCEU !!!\033[m')

    elif (n1+pc) % 2 != 0 and n2[0] == 'I':
        print(f'Eu escolhi o número {pc} e você {n1}.Total deu {n1+pc} IMPAR \033[32mVOCÊ VENCEU !!!\033[m')


    else:
        break

if (n1+pc) % 2 != 0:
    print(f'Eu escolhi o número {pc} e você {n1}.Total deu {n1+pc} IMPAR \033[31mVOCÊ PERDEU !!!\033[m')

if (n1+pc) % 2 == 0:
    print(f'Eu escolhi o número {pc} e você {n1}.Total deu {n1+pc} PAR \033[31mVOCÊ PERDEU !!!\033[m')

if cont == 1:
    print(f'Você jogou \033[33m{cont}\033[m vez.')
else:
    print(f'Você jogou \033[33m{cont}\033[m vezes.')

