from random import randint
from time import sleep
valores = []

def sorteio(lst):
    for c in range(0,5):
        lst.append(randint(1,10))
    print(f'Sorteando os 5 valores da lista:',end=' ')
    for c in lst:
        print(c,end=' ')
        sleep(0.3)
    print('OK!')

def somaPar(lst):
    soma = 0
    for c in lst:
        if c % 2 ==0:
            soma += c
    print(f'Somando os valores pares de {lst}, temos {soma}.')

sorteio(valores)
somaPar(valores)
