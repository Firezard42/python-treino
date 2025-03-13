from random import randint
from time import sleep
import operator
jogo = {}
raking = {}

print('Valores sorteados:')
for c in range(1,5):
    sleep(0.5)
    jogo[f'jogador{c}'] = randint(1,6)
    print(f'Jogador{c} tirou  {jogo[f'jogador{c}']} no dado.')

raking = dict(sorted(jogo.items(), key=operator.itemgetter(1),reverse=True)) #use o itemgetter para organizar um dicionario, ele faz parte da biblioteca operator
#use o reverse=True para colocar o dicionario ao contrario  #o 0 no itemgetter representa key e o 1 representa valor
podio = 1
print('=-'*30)
print('Ranking dos jogadores:')
for k,v in raking.items():
    sleep(0.5)
    print(f'{podio}ºLugar: {k} com {v}')
    podio += 1