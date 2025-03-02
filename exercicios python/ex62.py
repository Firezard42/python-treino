p1 = int(input('Qual é o primeiro termo da PA ? '))
r = int(input('Qual é a razão da PA ? '))
termo =  p1 + (10-1) * r

while p1 <= termo:
    print(p1)
    p1 = p1+r