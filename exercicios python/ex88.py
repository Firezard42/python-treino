from time import sleep
from random import randint
mega = []
mega2 = []
print('=-'*30)
print('\033[32mTIGRINHO DA SORTE\033[m'.center(65))
print('=-'*30)

n = int(input('Quantos jogos você quer que eu sorteie ? '))
n2 = 0

for c in range(0,n):
    for c2 in range(0,6):
        while True:
            n2 = randint(1,60)
            if n2 not in mega2:
                mega2.append(n2)
                break
    mega2.sort()
    mega.append(mega2[:])
    mega2.clear()

print(f'LANÇANDO AS {n} CARTADAS PAIH...'.center(65))
for e,c in enumerate(mega):
    sleep(0.5)
    print(f'Jogo {e+1}: {c}')