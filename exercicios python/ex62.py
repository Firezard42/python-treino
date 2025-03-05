p1 = int(input('Qual é o primeiro termo da PA ? '))
r = int(input('Qual é a razão da PA ? '))
termo =  p1 + (10-1) * r
termo2 = 1
cont = 0

while termo2 != 0:
    while p1 <= termo:
        print(f'{p1} -> ',end='')
        p1 = p1+r
        cont += 1
    termo2 = int(input('Você deseja vê mais quantos termos ? '))
    if termo2 != 0:
        termo = p1 + (termo2 - 1) * r

print(F'PROGRESSÃO FINALIZADA COM {cont} TERMOS MOSTRADOS.')


