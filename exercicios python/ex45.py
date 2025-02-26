from random import randint
import time

print('='*13,'JOKENPOOOOOO','='*13)
n1 = int(input('[0]PEDRA\n[1]PAPEL\n[2]TESOURA\nEscolha uma opção: '))
jogo = ['pedra','papel','tesoura']
n2 = randint(0,2)
if n1 in [0,1,2]:
    print('JO..')
    time.sleep(0.5)
    print('KEN...')
    time.sleep(0.5)
    print('POOOO!!!!')
    if n1 == 0 and n2 == 1 or n1 == 2 and n2 == 0 or n1 == 1 and n2 == 2:
        print('=-'*10)
        print(f'O computador jogou {jogo[n2]}')
        print(f'O jogador jogou {jogo[n1]}')
        print('=-' * 10)
        print('\033[0;31mO computador venceu\033[m')


    elif n2 == 0 and n1 == 1 or n2 == 2 and n1 == 0 or n2 == 1 and n1 == 2:
        print('=-' * 10)
        print(f'O computador jogou {jogo[n2]}')
        print(f'O jogador jogou {jogo[n1]}')
        print('=-' * 10)
        print('\033[0;32mo jogador venceu\033[m')

    else:
        print('=-' * 10)
        print(f'O computador jogou {jogo[n2]}')
        print(f'O jogador jogou {jogo[n1]}')
        print('=-' * 10)
        print('\033[0;33mfoi um empate\033[m')

else:
    print('\033[0;31mOPÇÃO INVÁLIDA\033[m')