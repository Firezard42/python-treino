p1 = int(input('Qual é o primeiro termo da PA ? '))
r = int(input('Qual é a razão da PA ? '))

for c in range(1,11):
    termo = p1+(c-1)*r
    print(f'{termo}',end=' -> ')

print('ACABOU')