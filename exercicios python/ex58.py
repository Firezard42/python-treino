from time import sleep
from random import randint
print('Sou o computador, e vou pensar em um número de 0 a 10 e você vai tentar adivinhar, OK ?')
print('PENSANDO',end='')
print('.',end='')
sleep(0.5)
print('.',end='')
sleep(0.5)
print('.')
computador = randint(0,10)
jogador = int(input('PRONTO, PENSEI !!!, agora me diga qual foi o número que eu pensei ? '))
cont = 1

while computador != jogador:
    print(f'\033[31mQUEEE BUROO, você errou feio\033[m')
    cont = cont+1
    jogador = int(input('Outra chance, tenta advinhar outra vez. Que número eu pensei ? '))

print(f'O número pensado foi {computador}')
if cont > 1:
    print(f'\033[32mPARABÉNS VOCÊ ME VENCEU, e só demorou {cont} tentativas!!!\033[m')
else:
    print(f'\033[32mPARABÉNS VOCÊ ME VENCEU, e foi de primeira !!!\033[m')
