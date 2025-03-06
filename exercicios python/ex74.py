from random import randint

n1 = randint(0,9)
n2 = randint(0,9)
n3 = randint(0,9)
n4 = randint(0,9)
n5 = randint(0,9)
maior = 0
menor = 0

sorteio = (n1,n2,n3,n4,n5)
print(f'Valores sorteados foram : ',end='')
for pos,c in enumerate(sorteio):
    print(c,end=' ')
    if pos == 0:
        maior = c
        menor = c
    if c > maior:
        maior = c
    if c < menor:
        menor = c

print('')
print(f'O Maior número foi : {maior}')
print(f'O Menor número foi : {menor}')